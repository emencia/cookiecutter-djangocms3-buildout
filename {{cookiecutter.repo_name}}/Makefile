PYTHON2_PATH=`which python2.7`
VIRTUALENV_PYTHON2_ARG= --python $(PYTHON2_PATH)

.PHONY: help install clean delpyc assets scss syncf5 tar_data import_db

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install -- to proceed to a new install of this project. Use clean command before if you want to reset a current install"
	@echo "  clean  -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  delpyc  -- to remove all *.pyc files, this is recursive from the current directory"
	@echo
	@echo "  tar_data   -- to dump applications datas to json files then put them in a tarball"
	@echo "  import_db  -- to import dumped datas, you should empty the database before"
	@echo
	@echo "  assets -- to minify all assets and collect static files"
	@echo "  scss -- to compile all SCSS stuffs with compass"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc
	rm -Rf bin include eggs lib parts django-apps-src develop-eggs local .installed.cfg compass/.sass-cache project/webapp_statics/.webassets-cache

assets:
	rm -f project/static/css/app.*.css project/static/css/modernizr.*.css project/static/js/app.*.js
	django-instance collectstatic --pythonpath=project/ --noinput
	django-instance assets build --pythonpath=project/
	django-instance collectstatic --pythonpath=project/ --noinput

scss:
	compass compile -c compass/config.rb compass/

install:
	virtualenv --no-site-packages --setuptools $(VIRTUALENV_PYTHON2_ARG) .
	bin/pip install 'setuptools==7.0'
	bin/pip install 'pip==1.5.6'
	mkdir -p eggs
	bin/python bootstrap.py --setuptools-version=7.0 --config-file=buildout.cfg --version=2.2.5
	bin/buildout -v
	bin/django-instance syncdb --all
	bin/django-instance migrate --fake

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

