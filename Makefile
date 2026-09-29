CODELAB_ID := github-copilot-workshop
OUT_DIR := $(CODELAB_ID)
TEMP_DIR := temp-export
CODELAB_ASSET_DIR := assets/codelab-elements
CODELAB_ASSET_PREFIX := ../../$(CODELAB_ASSET_DIR)
CODELAB_ASSETS := $(addprefix $(OUT_DIR)/$(CODELAB_ASSET_DIR)/,LICENSE codelab-elements.css native-shim.js custom-elements.min.js prettify.js codelab-elements.js)
CODELAB_HTML := $(wildcard $(OUT_DIR)/versions/*/index.html $(OUT_DIR)/custom/*/index.html)
PYTHON ?= python3

LATEST_VERSION := $(shell jq -r .defaultVersion $(OUT_DIR)/versions.json)

define rewrite-codelab-runtime
	sed -i.bak 's|https://storage.googleapis.com/claat-public/|$(CODELAB_ASSET_PREFIX)/|g' $(1)
	$(RM) $(addsuffix .bak,$(1))
endef

# export-codelab: claat export -> copy -> fix image/runtime paths -> clean up
#   $(1) = source Markdown
#   $(2) = output directory
define export-codelab
	go tool claat export -o $(TEMP_DIR) $(1)
	mkdir -p $(2)
	cp $(TEMP_DIR)/$(CODELAB_ID)/index.html $(2)/index.html
	# -i.bak is a portable form that works on both macOS (BSD sed) and Linux (GNU sed)
	sed -i.bak 's|src="img/|src="../../img/|g' $(2)/index.html
	$(RM) $(2)/index.html.bak
	$(call rewrite-codelab-runtime,$(2)/index.html)
	cp -r $(TEMP_DIR)/$(CODELAB_ID)/img/* $(OUT_DIR)/img/ 2>/dev/null || true
	$(RM) -r $(TEMP_DIR)
endef

.PHONY: export export-custom fix-codelab-runtime test test-browser

export export-custom fix-codelab-runtime: $(CODELAB_ASSETS)

# Export the latest version: make export
# Specify a different version: make export VERSION=v1.0.4
export: VERSION ?= $(LATEST_VERSION)
export:
	$(call export-codelab,workshop.md,$(OUT_DIR)/versions/$(VERSION))
	@echo "✅ Export of $(VERSION) completed"

# Export a custom version: make export-custom NAME=nri
export-custom:
	@test -n "$(NAME)" || (echo "❌ Specify NAME (example: make export-custom NAME=nri)" && exit 1)
	$(call export-codelab,workshop-$(NAME).md,$(OUT_DIR)/custom/$(NAME))
	@echo "✅ Export of the $(NAME) custom version completed"

# Repair existing exports without replacing historical workshop content.
fix-codelab-runtime:
	@test -n "$(CODELAB_HTML)" || (echo "No generated workshops found in $(OUT_DIR)" >&2; exit 1)
	$(call rewrite-codelab-runtime,$(CODELAB_HTML))

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_codelab_runtime.py' -v

test-browser:
	$(PYTHON) -m unittest discover -s tests -p 'test_codelab_browser.py' -v
