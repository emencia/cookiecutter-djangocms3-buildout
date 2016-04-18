.. _virtualenv: http://www.virtualenv.org/
.. _buildout: http://www.buildout.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter

=====
Usage
=====

This is quite simple, just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/emencia/cookiecutter-djangocms3-buildout

You will be prompted to anwser to some inputs about your project:

project_name
    [Default:*Project name*]

    Project name, should be unique into your repository host;
repo_name
    [Default:A slug created from project name]

    This will be used as the repository name;
repo_username
    [Default:*emencia*]

    Your username to use to push the repository;
repo_host
    [Default:*github.com*]

    The hostname of the repository host;
secret_key
    [Default:A random key]

    The secret key to use in Django settings, you should let the default value;

Then you will be prompted to define the application to enable within your project:

enable_accounts
    [Default:*no*]

    Enable the accounts component;
enable_contact_form
    [Default:*yes*]

    Enable a basic contact form with an optional captcha field;
enable_porticus
    [Default:*yes*]

    Enable Porticus application;
enable_slideshows
    [Default:*yes*]

    Enable Slideshows application;
enable_socialaggregator
    [Default:*no*]

    Enable Zinnia application;
enable_multiple_languages
    [Default:*no*]

    Enable CMS internationalization;

Take care that question about applications require a strict "yes" value to enable them, all other value are considered as a "no".

Created projects usage
**********************

Once a project has been created, you need to build it to use it. The process is simple. Do it in your project directory: ::

    make install

When it's finished, active the virtual environment: ::

    source bin/active

You can then use the project on the development server: ::

    django-instance runserver 0.0.0.0:8001

.. note::
        ``0.0.0.0`` is some sort of alias that mean "bind this server on my ip", so if your local ip is "192.168.0.42", the server will be reachable in your browser with the url ``http://192.168.0.42:8001/``.

.. note::
        Note the ``:8001`` that mean "bind the server on this port", this is a required part when you specify an IP. Commonly you can't bind on the port 80 so allways prefer to use a port starting from *8001*.

.. note::
        If you don't know your local IP, you can use ``127.0.0.1`` that is an internal alias to mean "my own network card", but this IP cannot be reached from other computers (because they have also this alias linked to their own network card).

The first required action is the creation of a CMS page for the home page and also you should fill-in the site name and its domain under ``Administration > Sites > Sites > Add site``.
