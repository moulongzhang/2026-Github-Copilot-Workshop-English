CODELAB_ID := github-copilot-workshop
OUT_DIR := $(CODELAB_ID)
TEMP_DIR := temp-export

LATEST_VERSION := $(shell jq -r .defaultVersion $(OUT_DIR)/versions.json)

# export-codelab: claat export -> copy -> fix image paths -> clean up
#   $(1) = source Markdown
#   $(2) = output directory
define export-codelab
	go tool claat export -o ./$(TEMP_DIR) $(1)
	mkdir -p $(2)
	cp $(TEMP_DIR)/$(CODELAB_ID)/index.html $(2)/index.html
	# -i.bak is a portable form that works on both macOS (BSD sed) and Linux (GNU sed)
	sed -i.bak 's|src="img/|src="../../img/|g' $(2)/index.html
	$(RM) $(2)/index.html.bak
	cp -r $(TEMP_DIR)/$(CODELAB_ID)/img/* $(OUT_DIR)/img/ 2>/dev/null || true
	$(RM) -r $(TEMP_DIR)
endef

.PHONY: export export-custom

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
