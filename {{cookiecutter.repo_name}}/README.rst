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

First you'll have to install `pip`_ and `virtualenv`_ on your system. Then some development libraries to compile some modules thereafter with `buildout`_.

Install them from your system packages:

* ``python-dev``;
* ``gettext``;
* ``gcc``;
* ``make``;
* ``libjpeg``;
* ``zlib``;
* ``libfreetype``;

Then install the project: ::

    make install

And finally activate the project virtual environment: ::

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

These files already exists with some settings commonly edited for their environment, so just fill them as you need.

Never, ever, edit settings directly in the mods for your environment requirements.

Usage
*****

You won't never use anymore the old ``managed.py`` script to launch Django instance but ``django-instance`` script instead. It will be installed in your ``bin/`` directory during the buildout process.

So to launch the Django development server with default settings, you will do : ::

    django-instance runserver 0.0.0.0:8001

To install database or apply Django migrations: ::

    django-instance migrate

See more details at `common topics around project usage <http://cookiecutter-djangocms3-buildout.readthedocs.io/en/latest/topics.html>`_
