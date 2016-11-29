.. _virtualenv: http://www.virtualenv.org/
.. _buildout: http://www.buildout.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter

=====
Usage
=====

Firstly, it will produce a new project structure then you will have to deploy it locally and finally enjoy it (webdesign integration, development, etc..).

Produced project structure
**************************

Just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/emencia/cookiecutter-djangocms3-buildout

You will be prompted to anwser to some inputs about your project and other inputs to enable some applications:

project_name
    [Default:*Project name*]

    Project name, should be unique into your repository host.
repo_name
    [Default:A slug created from project name]

    This will be used as the repository name.
repo_username
    [Default:*emencia*]

    Your username to use to push the repository.
repo_host
    [Default:*github.com*]

    The hostname of the repository host.
secret_key
    [Default:A random key]

    The secret key to use in Django settings, you should let the default value (a randomly generated string).
enable_accounts
    [Default:*no*]

    Enable the accounts component.
enable_contact_form
    [Default:*yes*]

    Enable a basic contact form with an optional captcha field.
enable_porticus
    [Default:*yes*]

    Enable Porticus application.
enable_slideshows
    [Default:*yes*]

    Enable Slideshows application.
enable_zinnia
    [Default:*no*]

    Enable Zinnia application.
enable_multiple_languages
    [Default:*no*]

    Enable CMS internationalization.
enable_https
    [Default:*yes*]

    Use a dedicated nginx configuration to enable https only through *let's encrypt*.
deploy_user
    [Default:*django*]

    System user where project will be deployed to (in its home directory).
deploy_host
    [Default: Empty]

    Host where to to deploy project using ssh.
changelog_mail_from
    [Default: Empty]

    Email 'from' adress use to send deployment informations.
changelog_mail_to
    [Default: Empty]

    Email 'to' adress use to send deployment informations.


.. NOTE::
   Usually you won't need to care about fields starting with ``repo_`` or ``deploy_`` and just let their default values.

Take care that question about applications require a strict ``yes`` value to enable them, all other value are considered as a ``no``.

Once structure has been created, a GIT repository will be initialized with the right remote url and a first commit, ready to push.

Deploy produced project
***********************

When project has been created, you need to install it to use it. Do it in your project directory: ::

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
        If you don't know your local IP, you can use ``127.0.0.1`` that is an internal alias to mean "my own network card", but this IP cannot be reached from other computers.

The first required action is the creation of a CMS page for the home page and also you should fill-in the site name and its domain under ``Administration > Sites > Sites > Add site``.
