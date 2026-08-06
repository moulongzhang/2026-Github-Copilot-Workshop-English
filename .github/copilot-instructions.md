## File Editing Rules

- Do not edit `github-copilot-workshop/index.html` (version selector)
- Do not directly edit `github-copilot-workshop/versions/*/index.html` (content for each version) either
- When updating standard workshop content, always edit `workshop.md`
- When updating a customer-specific variant, edit the corresponding `workshop-<NAME>.md` source

## Workshop Export

After editing workshop Markdown, follow `.agents/skills/export-workshop/SKILL.md` and use the Makefile-based export flow.

- Run `make export` to export `workshop.md` to the default version from `github-copilot-workshop/versions.json`
- Run `make export VERSION=v1.0.4` to export the standard workshop to a specific version
- Run `make export-custom NAME=nri` to export `workshop-nri.md` to `github-copilot-workshop/custom/nri/index.html`
- Use the same custom command with `NAME=denso` for the DENSO variant

When releasing a new standard version, run `make export VERSION=<new-version>`, add the new version to the beginning of the `versions` array in `github-copilot-workshop/versions.json`, and set `defaultVersion` to the new version.
