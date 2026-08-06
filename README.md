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

- **Go** (1.24 or later): Required to run claat
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

The `Makefile` exports Codelabs-formatted HTML, copies it to the correct output directory, fixes image paths, copies new images, and removes temporary files.

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
│   ├── versions/
│   │   └── <VERSION>/
│   │       └── index.html       # Generated standard workshop
│   ├── custom/
│   │   └── <NAME>/
│   │       └── index.html       # Generated customer-specific workshop
│   └── img/                     # Shared image files
├── assets/                      # Other assets
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

### Example: Deploying to GitHub Pages

```bash
# Push the contents of the github-copilot-workshop/ directory to the gh-pages branch
git subtree push --prefix github-copilot-workshop origin gh-pages
```

## 📖 Reference Links

- [Google Codelabs Tools](https://github.com/googlecodelabs/tools)
- [Codelabs Formatting Guide](https://github.com/googlecodelabs/tools/blob/main/FORMAT-GUIDE.md)
- [GitHub Copilot Documentation](https://docs.github.com/copilot)

## 📄 License

For the license of this workshop content, please refer to the LICENSE file in the repository.

## 🤝 Contributing

Suggestions for improvements and fixes to the workshop are welcome via Issues and Pull Requests.
