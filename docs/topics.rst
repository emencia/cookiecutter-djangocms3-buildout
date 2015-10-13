.. _intro_tips:
.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/
.. _Django: https://www.djangoproject.com/
.. _Foundation: http://foundation.zurb.com/
.. _Compass: http://compass-style.org/
.. _SCSS: http://sass-lang.com/
.. _rvm: http://rvm.io/
.. _rvm gemsets: https://rvm.io/gemsets
.. _Icomoon: http://icomoon.io/
.. _django-assets: http://django-assets.readthedocs.org/en/latest/
.. _webassets: http://webassets.readthedocs.org/en/latest/
.. _yuicompressor: http://yui.github.io/yuicompressor/
.. _Gestus client: https://github.com/sveetch/Gestus-client
.. _PO-Projects client: https://github.com/sveetch/PO-Projects-client
.. _Dr Dump: https://github.com/emencia/dr-dump
.. _emencia-recipe-drdump: https://github.com/emencia/emencia-recipe-drdump
.. _Django Icomoon: https://github.com/sveetch/django-icomoon

==================================
Common topics around project usage
==================================

Additionally to `Django`_ a created project is based on many other tools you should know, here are their topics.

RVM
***

`rvm`_ is somewhat like what `virtualenv`_ is to Python: a virtual environment. 

Difference is that it's intended for parallel installations of different **Ruby** versions without mixing gems (the **Ruby** application packages) from all Ruby version. In our scenario, it allows you to install a recent version of **Ruby** without affecting your system installation.

This is not required, just an usefull tip to know when developing on old systems with outdated packages or to be able to develop on various projects that don't share the same Compass/Foundation versions.

Gem sets
--------

Another usefull feature from `rvm`_, it allows you to have multiple environments for specific Ruby versions, each of those environments will have their own Gems (that is called a Gemset).

This is really usefull for case where you have to manage projects which depends on differents Foundation versions so you don't have to scratch your head with dependancies conflicts and so be able to develop on multiple Foundation versions.

So once rvm is installed you can do the following command: ::

    rvm list gemsets

It should displays the following results: ::

    rvm gemsets

       ruby-1.9.3-p545 [ x86_64 ]
       ruby-1.9.3-p545@global [ x86_64 ]
    => ruby-2.1.1 [ x86_64 ]
       ruby-2.1.1@global [ x86_64 ]

Ruby version may depends on your system. The current enabled Ruby version is prefixed with ``=>``.

Our sample scenario is Ruby version 2.1.1 with Foundation 5.4.x installed that depends on Compass 0.12.x or better and we need to be able to work also with Foundation 5.5.x that depends on Compass 1.x or better.

So first create the new Gemset to receive Foundation 5.5.x install, we will call it ``foundation55``: ::

    rvm gemset create foundation55

It should results on something like that: ::

    ruby-2.1.1 - #gemset created /home/emencia/.rvm/gems/ruby-2.1.1@foundation55
    ruby-2.1.1 - #generating foundation55 wrappers.........

So now the ``foundation55`` gemset is created, we can switch to it: ::

    rvm 2.1.1@foundation55

This is a fresh new install with only very basic gems, you can see them doing (you can compare with default gemsets switching again to it): ::

    gem list --local

And finally we will install the needed gems: ::

    gem install sass -v 3.4.0
    gem install chunky_png -v 1.3.3
    gem install compass -v 1.0
    gem install foundation -v 1.0.4

It's done now you can compile SCSS using Foundation 5.5.x. If you want to switch back on the gemset to compile Foundation 5.4.x, you just have to do: ::

    rvm 2.1.1

More details can be finded on documentation `rvm gemsets`_.

Usefull various commands
------------------------

*This sample use the scenario previously saw in `Gem sets`_.*

List the installed gems on the current environment: ::

    gem list --local

Launch a minimal webserver to display some usefull details about installed gems (it will be reachable in your webbrowser using the machine IP and port 8808): ::

    gem server -b 0.0.0.0

Want to empty a gemsets from all installed gems (except the basic ones): ::

    rvm gemset empty foundation55

Backup your gems list to a file: ::

    rvm gemset export foundation55.gems

Import your backuped gem list file: ::

    rvm gemset import foundation55.gems

Compass
*******

`Compass`_ is a **Ruby** tool used to compile `SCSS`_ sources in **CSS**.

By default, a `Django`_ project has its `SCSS`_ sources in the ``compass/scss/`` directory. The CSS `Foundation`_ framework is used as the database.

A recent install of Ruby and Compass is required first for this purpose (see `RVM`_ if your system installation is not up to date).

Once installed, you can then compile the sources on demand. Simply go to the ``compass/`` directory and launch this command: ::

    compass compile

When you are working uninterruptedly on the sources, you can simply launch the following command: ::

    compass watch

`Compass`_ will monitor the directory of sources and recompile the modified sources automatically.

By default the ``compass/config.rb`` configuration file (the equivalent of `settings.py`` in `Django`_) is used. If needed, you can create another one and specify it to `Compass`_ in its command (for more details, see the documentation).

Webfonts
********

Often, we use webfonts to display icons instead of images because this is more flexible to use (can take any size without to re-upload it) and results on less files. It's also more *CSS friendly*.

We use `Icomoon`_ service to build webfont because we can centralize their sources and the service generate a clean ZIP archive containing all needed stuff (all font kind, icon manifest, sample css, etc..).

Within our project We manage it through `Django Icomoon`_ to deploy webfont updates (using the downloaded ZIP) and to display an icon gallery.

.. NOTE::
   `Django Icomoon`_ usage is a new feature (see History for details), it may not be allready configured in your project if too old. But you can easily add it to, it should be compatible from Django '1.4.x' to '1.8.x'.


Just download the webfont ZIP from your `Icomoon`_ project, put it in your Django project and use the command line (adjust zip file path if needed): ::

    django-instance icomoon_deploy Default icomoon.zip

Font files will be deployed to their directory in statics (defined in mod settings) then a SCSS file will be generated so you can directly recompile them to build your CSS.

When it's done you can reach the gallery on: ::

    /icomoon/
    
.. warning::
   You need to be authenticated to view the gallery.

.. NOTE::
   There is allready a default webfont installed in your project with some default used icons like those ones required for **Slick.js** plugin. 

Assets management
*****************

Why
---

In the past, assets management was painful with some projects, because their includes was often divided in many different templates. This was causing issues to update some library or retrieve some code.

Often it resulted also in pages loading dozen of asset files and sometime much more. This was really a bad behavior because it slowed pages loading and added useless performance charge on the web server.

This is why we use an **asset manager** called `django-assets`_ which is a subproject of `webassets`_. Firstly read the `webassets`_ documentation to understand how is working its **Bundle** system. Then you can read the `django-assets`_ that is only related about `Django`_ usage with the settings, templatetags, etc..

How it works
------------

Asset managers generally perform two tasks :

* Regroup some kind of files together, like regrouping all Javascript files in an unique file;
* Minimize the file weight with removing useless white spaces to have the code on unique line;

Some asset manager implement this with their own file processor, some other like `webassets`_ are just "glue" between the files and another dedicated *compiler* like `yuicompressor`_.

Environments
------------

Asset management is really useful within integration or production environments and so when developing, the manager is generally disabled and the files are never compiled, you can verify this with looking at your page's source code.

make assets
-----------

Project have a ``make assets`` command that is useful **on integration and production environment** to deploy and update your assets in the ``static/`` directory. In fact **this command is always required in these environments** when you deploy a new update. Also you should never use it on development environment because it can cause you many troubles.

What does this command :

#. Remove some previous minified assets;
#. Collecting all static files from your project and installed apps to your ``settings.STATIC_ROOT`` directory;
#. Use `django-assets`_ to *compile* all defined bundles using previously collected files;
#. Re-collecting static files again to collect the compiled bundle files;

Static files directories
------------------------

In your ``settings.py`` file you should see :

..  sourcecode:: python
    
    STATIC_ROOT = join(PROJECT_PATH, 'static')

It define the *front* static file directory. But **never put yourself a file in this directory**, it is **reserved** for collected files in **integration and production environment** only.

All static files sources will go in the ``project/webapp_statics`` directory, it is defined in the *assets* mod:

..  sourcecode:: python
    
    ASSETS_ROOT = join(PROJECT_PATH, 'webapp_statics/')
    STATICFILES_DIRS += (ASSETS_ROOT,)

This way, we allways have separated directories for the sources and the compiled files. This is required to never commit compiled files and avoid conflicts between development and production environments.

The rule
--------

Never, ever, put CSS stylesheets in your templates, NEVER. You can forget them and they will be deployed in production and forgeted, this can be painful for other developers that coming after you. So **always add CSS stylesheets by the way of SCSS sources** using `Compass`_.

For Javascript code this is different, sometime we need to generate some code using `Django`_ templates for some specific cases. But if you use a same Javascript code in more than one template (using inheriting or so), you must move the code to a Javascript file.

Developers should never have to search in templates to change some CSS or Javascript code that is used in more than one page.

Developing application
**********************

Sometimes, you will need to develop some new app package or improve them without to embed them within the project.

You have two choices to do that:

* Use ``develop`` buildout variable to simply add your app to the developped apps, your app have to exists at the root of buildout project;
* Use ``vcs-extend-develop`` buildout variable to define a repository URL to the package sources;

Even they have the same base name *develop*, these two ways are differents:

* The first one simply add a symbolic link to the package in your Python install without to manage it as an installed eggs, it will be accessible as a Python module installed in the Python virtual environment. This method does not require that your app have a repository or have been published on PyPi;
* The second one install the targeted package from a given repository instead of a downloaded package from PyPi, it act like an installed eggs but from which you can edit the source and publish to the repository. And so your app name have to be defined in the buildout's egg variable, buildout will see it in ``vcs-extend-develop`` and will not try to install it from PyPi but from the given repository url;

In all ways, your apps is allways a full package structure that mean this is not a simple Python module, but its package structure containing stuff like ``README`` file and ``setup.py`` at the base of the directory then the Python module containing the code. Trying to use a simple Python module as a develop app will not work.

Which one to use and when
-------------------------

* If you want to **develop a new package**, it's often much faster to create its package directory structure at the root of your buildout project then use it within ``develop``. You would move it to ``vcs-extend-develop`` when you have published it;
* If you want to **develop an allready published package**, you will use ``vcs-extend-develop`` with its repository url, this so you will be able to edit it, commit changes then publish it;

Most of Emencia's apps are allready setted within ``vcs-extend-develop`` in the buildout config for development environment (``development.cfg``) but disabled, just uncomment the needed one.

Take care, an Egg that is installed from a repository url is validated on its version number if defined in the ``versions.cfg``, and so if your develop egg contains a version number less than the one defined in ``versions.cfg``, buildout will try to get the most recent version from PyPi, so allways manage the app version number.

PO-Projects
***********

**It aims to ease PO translations management** between developpers and translation managers. 

The `PO-Projects client`_ is pre-configured in all created projects but disabled by default. When enabled, its config file is automatically generated (in ``po_projects.cfg``), don't edit this file because it will be regenerated each time buildout is used.

The principe is that **developpers and translators does not have anymore to directly exchange PO files**. The developpers update the PO to the translation project on PO-Project webservice, translators update translations on PO-Project service frontend and developpers can get updated PO from the webservice.

To use it, you will have first to enable it in the buildout config, to install the client package, fill the webservice access and buildout part. Then when it's done, you have to create a project on PO-Project webservice using its frontend, then each required language for translation using the same locale names that the ones defined in the project settings.

There is only two available actions from the client :

Push action
    The ``push`` action role is to send updated PO (from `Django`_ extracts) from the project to the PO-Project webservice.
    
    Technically, the client will archive the locale directory into a tarball then send it to the webservice, that will use it to update its stored PO for each defined locales.
    
    Common way is (from the root of your project): ::
    
        cd project
        django-instance makemessages -a
        cd ..
        po_projects push


Pull action
    The ``pull`` action role is to get the updated translations from the webservice and install into the project.
    
    Technically, the client will download a tarball of the latest locale translations from the webservice and deploy it to your project, note that it will totally overwrite the project's locale directory.
    
    Common way is (from the root of your project): ::
    
        po_projects pull
        
    Then reload your webserver.

Note that the client does not manage your repository, each time you change your PO files (from `Django`_ ``makemessages`` action or ``pull`` client action) you still have to commit them.

Gestus
******

The `Gestus client`_ is pre-configured in all created projects, its config file is automatically generated (in ``gestus.cfg``), don't edit it because it will be regenerated each time buildout is used.

You can register your environment with the following command : ::

    gestus register

Remember this should only be used in integration or production environment and you will have to fill a correct accounts in the ``EXTRANET`` part.

Dr Dump
*******

`Dr Dump`_ is an utility to help you to dump and load datas from your `Django`_ project's apps. It does not have any command line interface, just a buildout recipe (`emencia-recipe-drdump`_) that will generate some bash scripts (``datadump`` and ``dataload``) in your ``bin`` directory so you can use them directly to dump your data into a ``dumps`` directory.

If the recipe is enabled in your buildout config (this is the default behavior), its bash scripts will be generated again each time you invoke a buildout.

Buildout will probably remove your dumps directory each time it re-install Dr Dump and Dr Dump itself will overwrite your dumped data files each time you invoke it dump script. So remember backup your dumps before doing this.

Note that Dr Dump can only manage app that it allready know in the used map, if you have some other packaged app or project's app that is not defined in the map you want to use, you have two choices :

* Ask to a repository manager of Dr Dump to add your apps, for some *exotic* or uncommon apps it will probably be refused;
* Download the map from the repository, embed it in your buildout project and give its path into the ``dependancies_map`` recipe variable so it will use it.

The second one is the most easy and flexible, but you will have to manage yourself the map to keep it up-to-date with the original one.
