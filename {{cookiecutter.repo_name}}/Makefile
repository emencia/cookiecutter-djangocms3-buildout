PYTHON2_PATH=`which python2.7`
VIRTUALENV_PYTHON2_ARG= --python $(PYTHON2_PATH)
FOUNDATION_VERSION=6.3.1
PROJECTDIR=project
STATICDIR=$(PROJECTDIR)/webapp_statics

.PHONY: help install install-dev install-foundation clean clean-foundation delpyc delminifiedassets assets tar_data import_db reload

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install              -- to proceed to a new install of this project. Use clean command before if you want to reset a current install"
	@echo "  install-dev          -- to proceed to a new install of this project with additional sources for development"
	@echo "  install-foundation   -- to install (or re-install) and deploy Foundation sources"

	@echo "  clean                -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  delpyc               -- to remove all *.pyc files, this is recursive from the current directory"
	@echo "  delminifiedassets    -- to remove minified assets from leading assets bundles"
	@echo
	@echo "  assets               -- to minify all assets and collect static files"
	@echo
	@echo "  tar_data             -- to dump applications datas to json files then put them in a tarball"
	@echo "  import_db            -- to import dumped datas, you should empty the database before"
	@echo
	@echo "  reload               -- to reload uwsgi instance (for integration and production only)"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

delminifiedassets:
	@echo "* Cleaning previous minifications"
	@rm -f $(STATICDIR)/css/app.*.css $(PROJECTDIR)/static/css/app.*.css
	@rm -f $(STATICDIR)/js/app.*.js $(PROJECTDIR)/static/js/app.*.js
	@rm -f $(STATICDIR)/js/modernizr.*.js $(PROJECTDIR)/static/js/modernizr.*.js

clean: delpyc delminifiedassets clean-foundation
	rm -Rf bin pip-selfcheck.json gestus.cfg po_projects.cfg include eggs lib parts django-apps-src develop-eggs local .installed.cfg compass/.sass-cache $(STATICDIR)/.webassets-cache

clean-foundation:
	rm -Rf foundation-sites
	rm -Rf $(STATICDIR)/js/foundation
	rm -Rf sass/foundation6

assets: delminifiedassets
	@echo "* Apply minifications"
	django-instance collectstatic --pythonpath=$(PROJECTDIR)/ --noinput
	django-instance assets --pythonpath=$(PROJECTDIR)/ build
	django-instance collectstatic --pythonpath=$(PROJECTDIR)/ --noinput

init:
	virtualenv --no-site-packages --setuptools $(VIRTUALENV_PYTHON2_ARG) .
	mkdir -p eggs

pre_build:
	bin/pip install 'setuptools>=19.1'
	bin/pip install 'pip>=7.1.2'
	bin/pip install 'zc.buildout==2.5.0'

build:  pre_build
	bin/buildout -v

build_integration:  pre_build
	bin/buildout -v -c integration.cfg

build_production:  pre_build
	bin/buildout -v -c production.cfg

install: init build
	bin/django-instance migrate
	bin/django-instance createsuperuser

install-dev: install install-foundation syncf5

install_integration: init build_integration
	bin/django-instance migrate
	bin/django-instance createsuperuser

install_production: init build_production
	bin/django-instance migrate sites || true
	bin/django-instance migrate

install-foundation: clean-foundation
	@echo "* Download Foundation $(FOUNDATION_VERSION) archive;"
	wget https://github.com/zurb/foundation-sites/archive/$(FOUNDATION_VERSION).tar.gz
	@echo "* Open archive;"
	tar xvzf $(FOUNDATION_VERSION).tar.gz
	mv foundation-sites-$(FOUNDATION_VERSION) foundation-sites
	@echo "* Delete archive;"
	rm -Rf $(FOUNDATION_VERSION).tar.gz
	@echo "* Use 'bower' to get Foundation dependencies"
	cd requirements/foundation6 && bower install
	@echo "* Copy Foundation Javascript files into project statics"
	mkdir -p $(STATICDIR)/js/foundation/vendor
	cp -r foundation-sites/dist/js/plugins $(STATICDIR)/js/foundation/plugins
	rm -f $(STATICDIR)/js/foundation/plugins/*.min.js
	cp -r foundation-sites/vendor/jquery/dist/jquery.js $(STATICDIR)/js/foundation/vendor/
	cp -r foundation-sites/vendor/modernizr/modernizr.js $(STATICDIR)/js/foundation/vendor/
	cp -r foundation-sites/vendor/jquery.cookie/jquery.cookie.js $(STATICDIR)/js/foundation/vendor/
	cp -r foundation-sites/vendor/what-input/dist/what-input.js $(STATICDIR)/js/foundation/vendor/
	@echo "* Updating Foundation SASS sources and dependencies"
	cp -r foundation-sites/scss sass/foundation6
	cp -r foundation-sites/_vendor/normalize-scss sass/
	cp -r foundation-sites/_vendor/sassy-lists sass/
	@echo "* Fix hardcoded paths in Foundation SASS sources"
	sed -i 's|\.\./_vendor/|\.\./|g' sass/foundation6/foundation.scss

scss:
	@echo "- Compile '$(STATICDIR)/css/app.css' from 'sass/scss/app.scss'"
	@sassc --include-path=sass/bourbon --include-path=sass/foundation6 sass/scss/app.scss $(STATICDIR)/css/app.css
	@echo "- Compile '$(STATICDIR)/css/minimal.css' from 'sass/scss/minimal.scss'"
	@sassc --include-path=sass/bourbon --include-path=sass/foundation6 sass/scss/minimal.scss $(STATICDIR)/css/minimal.css
	@echo "- Compile '$(STATICDIR)/css/ckeditor.css' from 'sass/scss/ckeditor.scss'"
	@sassc --include-path=sass/bourbon --include-path=sass/foundation6 sass/scss/ckeditor.scss $(STATICDIR)/css/ckeditor.css
	@echo "> Finished"

tar_data:
	@echo "Running data dump"
	@bin/datadump
	@echo "Running tarball create"
	@tar cvzf data_{{ cookiecutter.repo_name }}.tar.gz dumps $(PROJECTDIR)/media/

import_db:
	@bin/django-instance migrate
	@echo "Running data loading from dump directory"
	@bin/dataload

rm_sqlite:
	@rm database.sqlite3

reset_sqlite: rm_sqlite import_db

reload:
	echo r > var/uwsgi.fifo

test:
	@bin/django-instance test

flake8:
	@bin/flake8 project
