import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "github-copilot-workshop"
REMOTE = "https://storage.googleapis.com/claat-public/"
LOCAL = "../../assets/codelab-elements/"
ASSETS = (
    "codelab-elements.css",
    "native-shim.js",
    "custom-elements.min.js",
    "prettify.js",
    "codelab-elements.js",
)


class RuntimeReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.steps = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and "src" in attrs:
            self.urls.append(attrs["src"])
        elif tag == "link" and attrs.get("rel") == "stylesheet":
            self.urls.append(attrs["href"])
        elif tag == "google-codelab-step":
            self.steps += 1


class CodelabRuntimeTests(unittest.TestCase):
    def assert_local_runtime(self, page):
        html = page.read_text()
        self.assertFalse(REMOTE in html, f"{page} still depends on the external runtime")
        references = RuntimeReferences()
        references.feed(html)
        self.assertGreater(references.steps, 1)
        for asset in ASSETS:
            self.assertEqual(references.urls.count(LOCAL + asset), 1, str(page))
            self.assertTrue((page.parent / LOCAL / asset).is_file(), str(page))

    def run_make(self, *targets):
        result = subprocess.run(
            ["make", "--no-print-directory", "-f", str(ROOT / "Makefile"), *targets],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def prepare_site(self, directory):
        site = Path(directory) / "site"
        shutil.copytree(SITE / "assets", site / "assets")
        shutil.copyfile(SITE / "versions.json", site / "versions.json")
        (site / "img").mkdir()
        return site

    def test_all_published_workshops_use_local_runtime(self):
        versions = json.loads((SITE / "versions.json").read_text())
        self.assertIn(versions["defaultVersion"], [v["id"] for v in versions["versions"]])
        for version in versions["versions"]:
            self.assertTrue((SITE / version["path"]).is_file())
        pages = list(SITE.glob("versions/*/index.html")) + list(SITE.glob("custom/*/index.html"))
        self.assertTrue(pages)
        for page in pages:
            with self.subTest(page=page.relative_to(ROOT)):
                self.assert_local_runtime(page)

    def test_vendored_runtime_matches_tested_upstream_revision(self):
        self.assertIn("873fe39d02dc", (ROOT / "go.mod").read_text())
        # Git blob IDs from the immutable Japanese workshop repair, not the CDN.
        hashes = {
            "LICENSE": "420f8fbf3bd9e5114661f9026125e1c81d09138a",
            "codelab-elements.css": "936dc694e3f03b1b2802e9887aff49c404640c75",
            "codelab-elements.js": "be4adad0656423794e27bb3c39a315956c6f94b8",
            "custom-elements.min.js": "81bd847e57771671ed446d16b179ecc3c21f16e8",
            "native-shim.js": "2011d29a666a252023b81cb48896a9f911b0f688",
            "prettify.js": "10c9fb73d75268107f8273ebbb83aaae361d2a85",
        }
        for name, expected in hashes.items():
            with self.subTest(asset=name):
                data = (SITE / "assets/codelab-elements" / name).read_bytes()
                blob = b"blob " + str(len(data)).encode() + b"\0" + data
                self.assertEqual(hashlib.sha1(blob).hexdigest(), expected)

    def test_repair_preserves_content_and_selector_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            site = self.prepare_site(directory)
            selector = '<link rel="stylesheet" href="' + REMOTE + 'codelab-elements.css">'
            (site / "index.html").write_text(selector)
            pages = []
            original = (
                selector
                + "".join('<script src="' + REMOTE + name + '"></script>' for name in ASSETS[1:])
                + '<google-codelab-step label="English content">Keep this text.</google-codelab-step>'
            )
            for relative in ("versions/old/index.html", "custom/example/index.html"):
                page = site / relative
                page.parent.mkdir(parents=True)
                page.write_text(original)
                pages.append(page)
            for _ in range(2):
                self.run_make("fix-codelab-runtime", f"OUT_DIR={site}")
                for page in pages:
                    self.assertEqual(page.read_text(), original.replace(REMOTE, LOCAL))
                self.assertEqual((site / "index.html").read_text(), selector)
                self.assertEqual(list(site.rglob("*.bak")), [])

    def test_standard_and_custom_exports_use_local_runtime(self):
        with tempfile.TemporaryDirectory() as directory:
            site = self.prepare_site(directory)
            variables = [f"OUT_DIR={site}", f"TEMP_DIR={directory}/export"]
            self.run_make("export", *variables)
            default = json.loads((site / "versions.json").read_text())["defaultVersion"]
            self.assert_local_runtime(site / "versions" / default / "index.html")
            self.run_make("export", "VERSION=smoke-test", *variables)
            self.assert_local_runtime(site / "versions/smoke-test/index.html")
            for source in sorted(ROOT.glob("workshop-*.md")):
                name = source.stem.removeprefix("workshop-")
                with self.subTest(custom=name):
                    self.run_make("export-custom", f"NAME={name}", *variables)
                    self.assert_local_runtime(site / "custom" / name / "index.html")
            self.assertFalse((Path(directory) / "export").exists())
            self.assertEqual(list(site.rglob("*.bak")), [])


if __name__ == "__main__":
    unittest.main()
