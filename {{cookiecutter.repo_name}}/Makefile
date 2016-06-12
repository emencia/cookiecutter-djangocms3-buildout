PYTHON2_PATH=`which python2.7`
VIRTUALENV_PYTHON2_ARG= --python $(PYTHON2_PATH)
FOUNDATION_VERSION=5.5.3

.PHONY: help install install-dev install-foundation clean delpyc delminifiedassets assets syncf5 tar_data import_db reload

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install              -- to proceed to a new install of this project. Use clean command before if you want to reset a current install"
	@echo "  install-dev          -- to proceed to a new install of this project with additional sources for development"
	@echo "  install-foundation   -- to install (or re-install) Foundation sources"

	@echo "  clean                -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  delpyc               -- to remove all *.pyc files, this is recursive from the current directory"
	@echo "  delminifiedassets    -- to remove minified assets from leading assets bundles"
	@echo
	@echo "  assets               -- to minify all assets and collect static files"
	@echo "  syncf5               -- to update staticfiles with Foundation sources (use this is you upgrade Foundation sources)"
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
	@rm -f project/webapp_statics/css/app.*.css project/static/css/app.*.css
	@rm -f project/webapp_statics/js/app.*.js project/static/js/app.*.js
	@rm -f project/webapp_statics/js/modernizr.*.js project/static/js/modernizr.*.js

clean: delpyc delminifiedassets
	rm -Rf bin pip-selfcheck.json gestus.cfg po_projects.cfg include eggs lib parts django-apps-src develop-eggs local .installed.cfg compass/.sass-cache project/webapp_statics/.webassets-cache

assets: delminifiedassets
	@echo "* Apply minifications"
	django-instance collectstatic --pythonpath=project/ --noinput
	django-instance assets build --pythonpath=project/
	django-instance collectstatic --pythonpath=project/ --noinput

install-foundation:
	rm -Rf foundation5
	foundation new foundation5 --version=$(FOUNDATION_VERSION)
	@echo "Foundation v$(FOUNDATION_VERSION) sources has been installed, now you should synchronize assets using 'syncf5' action"

install:
	virtualenv --no-site-packages --setuptools $(VIRTUALENV_PYTHON2_ARG) .
	mkdir -p eggs
	bin/pip install 'setuptools>=19.1'
	bin/pip install 'pip>=7.1.2'
	bin/pip install 'zc.buildout==2.5.0'
	bin/buildout -v
	bin/django-instance migrate
	bin/django-instance createsuperuser

install-dev: install install-foundation syncf5

syncf5:
	@echo "* Updating jQuery sources"
	cp foundation5/bower_components/jquery/dist/jquery.js foundation5/bower_components/foundation/js/vendor/jquery.js
	@echo "* Updating Foundation static files"
	rm -Rf project/webapp_statics/js/foundation5
	cp -r foundation5/bower_components/foundation/js project/webapp_statics/js/foundation5
	@echo "* Cleaning vendor libs"
	rm -Rf project/webapp_statics/js/foundation5/vendor
	mkdir -p project/webapp_statics/js/foundation5/vendor
	@echo "* Getting the real sources for updated vendor libs"
	cp foundation5/bower_components/fastclick/lib/fastclick.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/foundation/js/vendor/jquery.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/jquery-placeholder/jquery.placeholder.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/jquery.cookie/jquery.cookie.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/modernizr/modernizr.js project/webapp_statics/js/foundation5/vendor/
	@echo "* Updating Foundation SASS sources"
	rm -Rf sass/foundation5
	cp -r foundation5/bower_components/foundation/scss sass/foundation5

scss:
	@echo "- Compile 'project/webapp_statics/css/app.css' from 'sass/scss/app.scss'"
	@sassc --include-path=sass/bourbon --include-path=sass/foundation5 sass/scss/app.scss project/webapp_statics/css/app.css
	@echo "- Compile 'project/webapp_statics/css/minimal.css' from 'sass/scss/minimal.scss'"
	@sassc --include-path=sass/bourbon --include-path=sass/foundation5 sass/scss/minimal.scss project/webapp_statics/css/minimal.css
	@echo "- Compile 'project/webapp_statics/css/ckeditor.css' from 'sass/scss/ckeditor.scss'"
	@sassc --include-path=sass/bourbon --include-path=sass/foundation5 sass/scss/ckeditor.scss project/webapp_statics/css/ckeditor.css
	@echo "> Finished"

tar_data:
	@echo "Running data dump"
	@bin/datadump
	@echo "Running tarball create"
	@tar cvzf data_{{ cookiecutter.repo_name }}.tar.gz dumps project/media/

import_db:
	@bin/django-instance syncdb --all --noinput
	@bin/django-instance migrate --fake
	@echo "Running data loading from dump directory"
	@bin/dataload

reload:
	echo r > var/uwsgi.fifo
