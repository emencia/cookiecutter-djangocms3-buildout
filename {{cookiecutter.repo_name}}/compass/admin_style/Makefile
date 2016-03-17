TARGET_DIR=../../project/webapp_statics/djangocms_admin_style/css/

.PHONY: help build

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  build              -- to build all 'admin_style' Sass stylesheets to project css directory"
	@echo

build:
	mkdir -p $(TARGET_DIR)
	sassc djangocms-admin.scss $(TARGET_DIR)djangocms-admin.css
	sassc djangocms-admin-frontend.scss $(TARGET_DIR)djangocms-admin-frontend.css
	sassc ie.scss $(TARGET_DIR)ie.css
