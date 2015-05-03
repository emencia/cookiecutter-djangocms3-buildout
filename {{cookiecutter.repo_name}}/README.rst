.. _buildout: http://www.buildout.org/
.. _pip: http://www.pip-installer.org/
.. _virtualenv: http://www.virtualenv.org/
.. _Django: http://www.djangoproject.com/
.. _cookiecutter-djangocms3-buildout: https://cookiecutter-djangocms3-buildout.readthedocs.org/

{{ '=' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

Install
*******

This Django project has been made with `cookiecutter-djangocms3-buildout`_  to be build with `buildout`_ system in a `virtualenv`_ environment.

You'll have to install `virtualenv`_ on your system and some `Devel libraries`_ to compile some modules thereafter with `buildout`_.

Install devel libraries using your ystem packages:

* Python development library (commonly known as ``python-devel``);
* ``libjpeg``;
* ``zlib``;
* ``libfreetype``;

Then you install the project: ::

    make install

Then activate the project virtual environment: ::

    source bin/activate

It's done for the default environment. If you need to use another environment, read below.

Buildout environments
---------------------

When the default environment has been correctly installed, just rebuild the project for your environment using the right configuration file.

For development environment: ::
   
    buildout -c development.cfg

For integration environment: ::
   
    buildout -c integration.cfg

For production environment: ::
   
    buildout -c production.cfg

With production and integration you'll have also to build the assets: ::

    make assets

Environment and Django settings
-------------------------------
   
Each environment has its own settings file to override default settings.

These files allready exists with some settings commonly edited for their environment, so just fill them as you need.

Never, ever, edit settings directly in the mods.

Usage
*****

You won't never use anymore the old ``managed.py`` script to launch Django instance but ``django-instance`` script instead that will be installed in your ``bin/`` directory during the buildout process.

So to launch the Django development server with defaut settings, you will do : ::

    django-instance runserver 0.0.0.0:8001
