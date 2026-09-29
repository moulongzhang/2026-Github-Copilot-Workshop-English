# GitHub Copilot Workshop

This repository manages Codelabs content for a GitHub Copilot workshop.

This is the English edition of the [Japanese GitHub Copilot Workshop](https://github.com/moulongzhang/2026-Github-Copilot-Workshop).

## 🌐 How to Access

The workshop content can be accessed at the following URL:

https://moulongzhang.github.io/2026-Github-Copilot-Workshop-English/github-copilot-workshop


## 📚 Overview

This is a hands-on workshop for learning the features of GitHub Copilot. It includes practical content such as developing new applications using Agent Mode.

In addition to the standard workshop, this repository includes customer-specific variants for BNS, DENSO, and NRI.

## 🛠️ How to Edit Workshop Content

This workshop is created using the [Google Codelabs](https://github.com/googlecodelabs/tools) format.

Clone this repository before editing the workshop:

```bash
git clone https://github.com/moulongzhang/2026-Github-Copilot-Workshop-English.git
cd 2026-Github-Copilot-Workshop-English
```

### Required Tools

- **Go** (1.26.3 or later, as declared in `go.mod`): Required to run claat
- **claat** (Codelabs as a Thing): Generates Codelabs-formatted HTML from Markdown files. Its version is pinned by the `tool` directive in `go.mod`
- **make**: Runs the workshop export tasks defined in `Makefile`
- **jq**: Reads the default version from `github-copilot-workshop/versions.json`

### Using claat

```bash
go tool claat --help
```

## 📝 Editing and Generating the Workshop

### 1. Editing Content

Edit the source file for the workshop you want to update:

| Workshop | Source file |
|---|---|
| Standard | `workshop.md` |
| BNS | `workshop-bns.md` |
| DENSO | `workshop-denso.md` |
| NRI | `workshop-nri.md` |

Write the content in Codelabs-formatted Markdown.

The following metadata is required at the beginning of each file:

```markdown
author: Your Name
summary: GitHub Copilot Workshop
id: github-copilot-workshop
categories: AI, Development
environments: Web
status: Published
feedback link: https://example.com/feedback
```

### 2. Generating HTML

The `Makefile` exports Codelabs-formatted HTML, copies it to the correct output directory, fixes image and runtime paths, copies new images, and removes temporary files. The Codelabs runtime is served from `github-copilot-workshop/assets/codelab-elements/`, not the external `claat-public` bucket, so a bucket outage cannot remove the workshop's navigation controls.

Export the standard workshop to the default version specified by `defaultVersion` in `github-copilot-workshop/versions.json`:

```bash
# Export the default version
make export
```

Export the standard workshop to a specific version:

```bash
# Export a specified version
make export VERSION=v1.0.4
```

Export a customer-specific workshop:

```bash
# Export the BNS variant
make export-custom NAME=bns
# Export the DENSO variant
make export-custom NAME=denso
# Export the NRI variant
make export-custom NAME=nri
```

The generated HTML is written to the following locations:

| Workshop | Output |
|---|---|
| Standard | `github-copilot-workshop/versions/<VERSION>/index.html` |
| Customer-specific | `github-copilot-workshop/custom/<NAME>/index.html` |

Always run the appropriate export command after editing `workshop.md` or `workshop-*.md`.

### 3. Preview

You can preview the generated content locally:

```bash
go tool claat serve
```

Open `http://localhost:9090` in your browser to view the generated workshop.

### 4. Make Targets

| Target | Description |
|---|---|
| `make export` | Export `workshop.md` to the current default version |
| `make export VERSION=<version>` | Export `workshop.md` to a specified version |
| `make export-custom NAME=<name>` | Export `workshop-<name>.md` to the matching custom output directory |
| `make fix-codelab-runtime` | Switch existing standard/custom exports to the local runtime without changing their content |
| `make test` | Check runtime assets, repair idempotence, and all Markdown export paths (Python 3, Go, and jq required) |
| `make test-browser` | Check desktop/mobile navigation and version selection in Chromium (Python Playwright required) |

The runtime matches the claat revision in `go.mod`; its provenance and license are recorded in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). Keep the runtime and claat revision in sync when upgrading.

To run the browser regression tests:

```bash
python3 -m pip install -r tests/requirements.txt
python3 -m playwright install chromium
make test-browser
```

If Google Chrome is already installed, use `PLAYWRIGHT_CHANNEL=chrome make test-browser` instead of downloading Chromium. Tests serve the repository under a GitHub Pages-style project path and block external runtime requests, exercising all standard and custom workshops without relying on the failed bucket.

The protected version-selector HTML is unchanged. Its unused external Codelabs stylesheet may still fail to load; the actual workshop UI runs in the iframe and uses only the local runtime.

### 5. Other Useful claat Commands

```bash
# Show help
go tool claat help

# Export in a specific format
go tool claat export -f html workshop.md

# Update existing content
go tool claat update workshop.md

# Export multiple files at once
go tool claat export *.md
```

## 📂 Directory Structure

```
.
├── README.md
├── Makefile
├── go.mod
├── go.sum
├── workshop.md
├── workshop-bns.md
├── workshop-denso.md
├── workshop-nri.md
├── github-copilot-workshop/
│   ├── index.html               # Version selector; do not edit directly
│   ├── versions.json            # Version metadata and default version
│   ├── assets/codelab-elements/  # Pinned, self-hosted Codelabs runtime
│   ├── versions/
│   │   └── <VERSION>/
│   │       └── index.html       # Generated standard workshop
│   ├── custom/
│   │   └── <NAME>/
│   │       └── index.html       # Generated customer-specific workshop
│   └── img/                     # Shared image files
├── bns/                         # Short-link redirect to the BNS workshop
└── registrations/               # Registration information
```

## 🏷️ Versioning Workflow

To release a new standard workshop version:

1. Export the workshop with the new version number:

   ```bash
   make export VERSION=<new-version>
   ```

2. Update `github-copilot-workshop/versions.json`:
   - Add the new version to the beginning of the `versions` array.
   - Set `defaultVersion` to the new version.

Do not edit `github-copilot-workshop/index.html` or generated files under `github-copilot-workshop/versions/*/index.html` directly. Make content changes in the Markdown source and regenerate the HTML with `make`.

## 🚀 Deployment

The contents of the generated `github-copilot-workshop/` directory can be deployed to GitHub Pages or any web server.

The Pages workflow (`.github/workflows/static.yml`) publishes the committed repository on pushes to `main` or a manual dispatch. Deployment waits for the shared Codelabs regression workflow to pass, including real exports and desktop/mobile browser checks. Pull requests run the same checks without deploying.

## 📖 Reference Links

- [Google Codelabs Tools](https://github.com/googlecodelabs/tools)
- [Codelabs Formatting Guide](https://github.com/googlecodelabs/tools/blob/main/FORMAT-GUIDE.md)
- [GitHub Copilot Documentation](https://docs.github.com/copilot)

## 📄 License

No license has been declared for this workshop content yet.

## 🤝 Contributing

Suggestions for improvements and fixes to the workshop are welcome via issues and pull requests.
