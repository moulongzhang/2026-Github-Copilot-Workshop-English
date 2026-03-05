# GitHub Copilot Workshop

This repository manages Codelabs content for a GitHub Copilot workshop.

## 🌐 How to Access

The workshop content can be accessed at the following URL:

https://moulongzhang.github.io/2026-Github-Copilot-Workshop-English/github-copilot-workshop


## 📚 Overview

This is a hands-on workshop for learning the features of GitHub Copilot. It includes practical content such as developing new applications using Agent Mode.

## 🛠️ How to Edit Workshop Content

This workshop is created using the [Google Codelabs](https://github.com/googlecodelabs/tools) format.

### Required Tools

- **claat** (Codelabs as a Thing): A tool that generates Codelabs-formatted HTML from Markdown files

### Installing claat

#### macOS

**Method: Using Homebrew (Recommended)**

```bash
brew install claat
```

### Verifying the Installation

```bash
claat version
```

## 📝 Editing and Generating the Workshop

### 1. Editing Content

Edit the `workshop.md` file. Write the content in Codelabs-formatted Markdown.

The following metadata is required at the beginning of the file:

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

Generate Codelabs-formatted HTML from the Markdown file:

```bash
# Basic generation
claat export workshop.md

# Generate with a specified output directory
claat export -o github-copilot-workshop workshop.md
```

The generated HTML will be output to the `github-copilot-workshop/` directory.

### 3. Preview

You can preview the generated content locally:

```bash
claat serve
```

Open `http://localhost:9090` in your browser to view the generated workshop.

### 4. Commonly Used Commands

```bash
# Show help
claat help

# Generate in a specific format
claat export -f html workshop.md

# Update existing content
claat update workshop.md

# Batch generate multiple files
claat export *.md
```

## 📂 Directory Structure

```
.
├── README.md                    # This file
├── workshop.md                  # Workshop source file
├── github-copilot-workshop/     # Generated Codelabs content
│   ├── index.html
│   ├── codelab.json
│   └── img/                     # Image files
├── assets/                      # Other assets
└── registrations/               # Registration information
```

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
