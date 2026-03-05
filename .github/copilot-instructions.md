## File Editing Rules

- Do not edit `github-copilot-workshop/index.html` (version selector)
- Do not directly edit `github-copilot-workshop/versions/*/index.html` (content for each version) either
- When updating content, always edit `workshop.md`

## Steps to Update workshop.md

1. Edit `workshop.md`
2. Update the latest version with the following commands:

```bash
# Generate in a temporary folder
claat export -o ./temp-export workshop.md

# Set the latest version number (e.g., v1.0.1)
LATEST_VERSION="v1.0.1"

# Copy to the latest version folder
cp temp-export/github-copilot-workshop/index.html "github-copilot-workshop/versions/${LATEST_VERSION}/index.html"

# Fix image paths (to display correctly inside iframes)
sed -i '' 's|src="img/|src="../../img/|g' "github-copilot-workshop/versions/${LATEST_VERSION}/index.html"

# Update with new images if any
cp -r temp-export/github-copilot-workshop/img/* github-copilot-workshop/img/ 2>/dev/null || true

# Delete the temporary folder
rm -rf temp-export

echo "✅ Update for ${LATEST_VERSION} is complete"
```

3. When releasing a new version:
   - Create a new version folder (e.g., `versions/v1.0.2/`)
   - Update `versions.json` to add the new version
   - Change `defaultVersion` to the new version
