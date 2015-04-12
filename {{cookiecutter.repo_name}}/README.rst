.. _Foundation: http://foundation.zurb.com/
.. _modular-scale: https://github.com/scottkellum/modular-scale
.. _Compass: http://compass-style.org/
.. _Django: http://www.djangoproject.com/
.. _rvm: http://rvm.io/
.. _yui-compressor: http://developer.yahoo.com/yui/compressor/
.. _django-debug-toolbar: http://github.com/django-debug-toolbar/django-debug-toolbar/
.. _django-admin-tools: http://pypi.python.org/pypi/django-admin-tools/
.. _django-assets: https://github.com/miracle2k/django-assets
.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org/

Install
=======

This project is made to be build with `buildout`_ system in a `virtualenv`_ environment.

So first you have to install `virtualenv`_ on your system, then you will need some `Devel libraries`_ on your system to compile some modules thereafter with `buildout`_.

For a quick test install :

    make install

Then you have to activate the project's virtual environment : ::

    source bin/activate

For development environment you also have to do this : ::
   
    buildout -c development.cfg

Or for integration environment you also have to do this (note that you have to build the assets) : ::
   
    buildout -c integration.cfg
    make assets

Or for production environment you also have to do this : ::
   
    buildout -c production.cfg
    make assets

Buildout environment configs and Django settings
************************************************
   
If you use the ``development.cfg`` or ``production.cfg`` config files with buildout, you will have to fill the appropriate settings.

With ``development.cfg`` you have to edit ``project/settings_development.py`` like this : ::

    from project.settings import *

    INTERNAL_IPS = () # Fill this to your machine IP (the client, not your server) enable django-debug-toolbar

    # Database access, only required if you don't want to use the sqlite3 database, else remove it
    DATABASES = {
        'default': {
            'HOST': 'localhost',
            'NAME': 'DATABASE_NAME',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'LOGIN',
            'PASSWORD': 'PASSWORD',
        }
    }

With ``production.cfg`` you have to edit ``project/settings_production.py`` file like this : ::

    from project.settings import *

    DEBUG = TEMPLATE_DEBUG = False

    ASSETS_DEBUG = False
    ASSETS_ROOT = STATIC_ROOT
    ASSETS_AUTO_BUILD = False

    # SMTP Settings sample to send Applications emails
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 25
    EMAIL_SUBJECT_PREFIX = '[YourProject] '

    # Database access
    DATABASES = {
        'default': {
            'HOST': 'localhost',
            'NAME': 'DATABASE_NAME',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'LOGIN',
            'PASSWORD': 'PASSWORD',
        }
    }

These files allready exists with some settings commonly edited for their environment, so just fill them as you need.

Never, ever, edit settings directly in the mods.

Devel libraries
***************

This is the devel libraries needed to compile some Python libraries, note that the package name can differ for your distribution.

For psycopg2 (a Postgresl driver for Python)
--------------------------------------------

* python
* libpq

For Pillow
----------

* python
* libjpeg
* zlib
* libfreetype

Foundation
**********

This project embed `Foundation`_ 5 sources installed from the `Foundation`_ app so you can update it from the sources if needed (and if you have installed the Foundation cli, see its documentation for more details). If you do so you will have to synchronise the updated sources in the project's static files with a command in the Makefile : ::

    make syncf5

This will update Javascripts sources in the static files but take care that it will clean the directory before, so never put your files in the directory ``project/webapp_statics/js/foundation5`` or they will be deleted.

**Take care that this is not a stable feature**, so you should be ready to fix some things (like assets bundles, directory structure, shellscript command in makefile) when updating between major Foundation versions.

For the `Foundation`_ SCSS sources, don't bother they are directly imported in the compass config, so you have nothing to care about.

The project also embed *Foundation 3* sources because they are used for some components in the Django administration that didn't migrate to Foundation 5, you should not have to worry about them.

Usage
=====

With the buildout install, you won't never use the common ``managed.py`` script to launch Django instance but ``django-instance`` script that was installed in you ``bin/`` directory during the buildout process.

So to launch the Django development server with defaut settings, you will do (from the ``project`` directory) : ::

    django-instance runserver 0.0.0.0:8001
