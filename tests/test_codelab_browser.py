from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import threading
import unittest
from urllib.parse import parse_qs, urlsplit

from playwright.sync_api import expect, sync_playwright

from test_codelab_runtime import REMOTE, ROOT, SITE


PROJECT_PATH = "/2026-Github-Copilot-Workshop-English"
VIEWPORTS = ({"width": 1440, "height": 1000}, {"width": 390, "height": 844})


class PagesHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if not self.path.startswith(PROJECT_PATH + "/"):
            self.send_error(404)
            return
        self.path = self.path[len(PROJECT_PATH):]
        super().do_GET()

    def log_message(self, format, *args):
        pass


class CodelabBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(
            ("127.0.0.1", 0), partial(PagesHandler, directory=str(ROOT))
        )
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.addClassCleanup(cls.stop_server)
        cls.origin = f"http://127.0.0.1:{cls.server.server_port}"
        cls.base = cls.origin + PROJECT_PATH + "/github-copilot-workshop/"
        cls.playwright = sync_playwright().start()
        cls.addClassCleanup(cls.playwright.stop)
        cls.browser = cls.playwright.chromium.launch(channel=os.environ.get("PLAYWRIGHT_CHANNEL"))
        cls.addClassCleanup(cls.browser.close)
        cls.versions = json.loads((SITE / "versions.json").read_text())

    @classmethod
    def stop_server(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    @contextmanager
    def page(self, viewport, selector=False):
        context = self.browser.new_context(viewport=viewport)
        page = context.new_page()
        page.set_default_timeout(10000)
        errors, local_failures, bucket_requests = [], [], []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on(
            "response",
            lambda response: local_failures.append(f"{response.status} {response.url}")
            if response.url.startswith(self.origin + "/") and response.status >= 400 else None,
        )
        page.on(
            "requestfailed",
            lambda request: local_failures.append(f"{request.failure} {request.url}")
            if request.url.startswith(self.origin + "/") else None,
        )

        def route_request(route):
            request = route.request
            if request.url.startswith(REMOTE):
                bucket_requests.append((request.url, request.frame == page.main_frame))
            if request.url.startswith(self.origin + "/"):
                route.continue_()
            else:
                route.abort()

        page.route("**/*", route_request)
        try:
            yield page
            self.assertEqual(errors, [])
            self.assertEqual(local_failures, [])
            # The protected selector retains one unused external stylesheet.
            for url, main_frame in bucket_requests:
                self.assertTrue(selector and main_frame, url)
                self.assertEqual(url, REMOTE + "codelab-elements.css")
        finally:
            context.close()

    def assert_step(self, frame, index):
        expect(frame.locator("google-codelab-step:visible")).to_have_count(1)
        expect(frame.locator("google-codelab-step").nth(index)).to_be_visible()
        self.assertEqual(urlsplit(frame.url).fragment, str(index))

    def assert_navigation(self, frame, mobile):
        expect(frame.locator("#next-step")).to_be_visible()
        self.assertTrue(frame.evaluate("!!customElements.get('google-codelab')"))
        steps = frame.locator("google-codelab-step")
        count = steps.count()
        self.assertGreater(count, 2)
        expect(frame.locator('#drawer a[href^="#"]')).to_have_count(count)
        self.assert_step(frame, 0)
        expect(frame.locator("#previous-step")).to_be_hidden()
        expect(frame.locator("#next-step")).to_be_in_viewport()
        frame.locator("#next-step").click()
        self.assert_step(frame, 1)
        expect(frame.locator("#previous-step")).to_be_in_viewport()
        frame.locator("#previous-step").click()
        self.assert_step(frame, 0)

        if mobile:
            expect(frame.locator("#menu")).to_be_in_viewport()
            frame.locator("#menu").click()
        expect(frame.locator('#drawer a[href="#2"]')).to_be_in_viewport()
        frame.locator('#drawer a[href="#2"]').click()
        self.assert_step(frame, 2)
        if mobile:
            self.close_drawer(frame)
            frame.locator("#menu").click()
        frame.locator(f'#drawer a[href="#{count - 1}"]').click()
        self.assert_step(frame, count - 1)
        expect(frame.locator("#done")).to_be_visible()
        expect(frame.locator("#next-step")).to_be_hidden()
        if mobile:
            self.close_drawer(frame)
        frame.locator("#previous-step").click()
        self.assert_step(frame, count - 2)
        if mobile:
            frame.locator("#menu").click()
        # All variants share a Codelab ID and therefore the saved progress key.
        frame.locator('#drawer a[href="#0"]').click()
        self.assert_step(frame, 0)
        if mobile:
            self.close_drawer(frame)

    def close_drawer(self, frame):
        # Codelabs keeps the drawer open after selection until an outside click.
        frame.locator("#main").click(position={"x": 300, "y": 100})
        expect(frame.locator("google-codelab")).not_to_have_attribute("drawer--open", "")

    def selected_frame(self, page, path):
        expect(page.locator("#version-selector")).to_have_value(path)
        expect(page.locator("#content-frame")).to_have_attribute("src", path)
        page.wait_for_function(
            """path => {
                const frame = document.querySelector('#content-frame').contentWindow;
                return frame.location.pathname.endsWith('/' + path)
                    && !!frame.customElements.get('google-codelab');
            }""",
            arg=path,
        )
        return page.locator("#content-frame").element_handle().content_frame()

    def test_all_standard_and_custom_workshops(self):
        paths = [version["path"] for version in self.versions["versions"]]
        paths += [str(path.relative_to(SITE)) for path in sorted(SITE.glob("custom/*/index.html"))]
        for viewport in VIEWPORTS:
            for path in paths:
                with self.subTest(viewport=viewport, path=path), self.page(viewport) as page:
                    page.goto(self.base + path, wait_until="networkidle")
                    self.assert_navigation(page, mobile=viewport["width"] < 800)

    def test_root_default_and_version_selection(self):
        default = next(v for v in self.versions["versions"] if v["id"] == self.versions["defaultVersion"])
        for viewport in VIEWPORTS:
            with self.subTest(viewport=viewport), self.page(viewport, selector=True) as page:
                page.goto(self.base, wait_until="networkidle")
                self.assert_navigation(self.selected_frame(page, default["path"]), viewport["width"] < 800)
                for version in self.versions["versions"]:
                    if version["id"] == default["id"]:
                        continue
                    page.locator("#version-selector").select_option(version["path"])
                    frame = self.selected_frame(page, version["path"])
                    self.assert_step(frame, 0)
                    self.assertEqual(parse_qs(urlsplit(page.url).query)["version"], [version["id"]])
                    self.assert_navigation(frame, viewport["width"] < 800)
                page.reload(wait_until="networkidle")
                self.assert_step(self.selected_frame(page, version["path"]), 0)

    def test_bns_short_link_and_step_deep_link(self):
        with self.page(VIEWPORTS[0]) as page:
            page.goto(self.origin + PROJECT_PATH + "/bns/", wait_until="networkidle")
            expect(page.locator("#next-step")).to_be_visible()
            self.assertTrue(urlsplit(page.url).path.endswith("/custom/bns/index.html"))
            self.assert_navigation(page, mobile=False)
            page.goto(self.base + "versions/" + self.versions["defaultVersion"] + "/index.html#2")
            self.assert_step(page, 2)
            page.reload(wait_until="networkidle")
            self.assert_step(page, 2)


if __name__ == "__main__":
    unittest.main()
