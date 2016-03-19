.. Never edit this file manually, instead edit its template in 
   'templates/project_structure.rst' and use 'make grab' to build 
   with mods documentations

.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Foundation: http://foundation.zurb.com/
.. _Compass: http://compass-style.org/
.. _SCSS: http://sass-lang.com/
.. _rvm: http://rvm.io/
.. _CKEditor: http://ckeditor.com/
.. _Django: https://www.djangoproject.com/
.. _Django CKEditor: https://github.com/divio/djangocms-text-ckeditor
.. _Dr Dump: https://github.com/emencia/dr-dump
.. _emencia-recipe-drdump: https://github.com/emencia/emencia-recipe-drdump

==================
Projects structure
==================

Projects are created with the many components that are available for use. These components are called **mods** and these mods are already installed and ready to use. You can enable or disable them, as needed.

django-instance
***************

This is the command installed to replace the old ``manage.py`` script in Django. ``django-instance`` is located into the ``project/bin`` directory and is aware of installed eggs from buildout.

Git ignore
**********

Project embeds many ``.gitignore`` files to avoid to commit some files into your repository.

Principle is to never commit files created from buildout (installed packages, app development sources, etc..), compiled static files, project media files and database.

Makefile
********

Project embeds a ``Makefile`` file that contains some usefull commands to build your project.

``install``
    to proceed to a new install of this project. Use clean command before if you want to reset a current install
``install-dev``
    to proceed to a new install of this project with additional sources for development
``install-foundation``
    to install (or re-install) Foundation 5 sources
``clean``
    to clean your local repository from all stuff created by buildout and instance usage
``delpyc``
    to remove all ``*.pyc`` files, this is recursive from the current directory
``assets``
    to minify all assets and collect static files
``scss``
    to compile all SCSS stuffs with compass
``syncf5``
    to update staticfiles with Foundation sources (use this is you upgrade Foundation sources)
``tar_data``
    to dump applications datas to json files then put them in a tarball
``import_db``
    to import dumped datas, you should empty the database before
``reload``
    to reload uwsgi instance (for integration and production only)

Compass+Foundation
******************

Default SCSS are made for `Foundation`_ (version 5.4.7) and compiled with `Compass`_ (version >= 0.12, <1.0). 

Shipped templates are integrated using `Foundation`_ components and created project embeds css compiled with the SCSS sources from the ``compass`` directory.

Adding application
******************

If you plan to integrate a new app into a project, always use the `buildout`_ system to ensure its portability (`pip`_ requirements file is not used in our system). 

To do this, just open and edit the ``buildout.cfg`` file to add the new egg name to be installed. For more details, read the `buildout`_ documentation.

Also it is always preferable to use the mods system to configure new added apps and keep the ``settings.py`` only for Django owned settings.

.. NOTE::
   Project contains a ``version.cfg`` file that define exact version to use for listed eggs in ``buildout.cfg``. All existing mods have their eggs defined in this file, if you need to enable a mod that you skipped during project creation, just find its egg name in ``version.cfg`` and add it to the eggs in ``buildout.cfg``.

How the Mods work
*****************

The advantage of centralizing app configurations in their mods is to safely gather together them distinctly from the Django basic settings (like SMTP config, database access, middlewares, etc..). Furthermore it is easier to enable or disable apps.

**To create a new mods**:

* Create a directory in ``project/mods_available/`` that contains at least one empty ``__init__.py`` and a ``settings.py`` to enable the app (using ``settings.INSTALLED_APPS``) in the project and potentially its settings and urls;
* The ``settings.py`` and ``urls.py`` files in this directory will be executed automatically by the project (the system loads them after the project ones so that a mods can overwrite the project initial settings and urls);
* N.B. With the Django ``runserver`` command, a change to these files does not reload the project instance; you need to relaunch it yourself manually;

**To enable a new mods**, you need to create its symbolic link (**a relative path** to the available mod) in ``project/mods_enabled``. To disable it, simply delete the symbolic link.

Since Django 1.8, every template settings are contained in their backend entry in ``settings.TEMPLATES``. We actually assume to only use the default Django template backend in our project. So mods will be able to manipulate template settings using the default backend that will be the index 0 of the backends list: ::

    TEMPLATES[0]['OPTIONS']['context_processors'] = ....

Trying to use the old template settings will result in an error.

Available mods
**************

accounts
--------

.. _Django reCaptcha: https://github.com/praekelt/django-recaptcha
.. _Django registration: https://github.com/macropin/django-registration

Enable `Django registration`_ and everything you need to allow users to register and to connect/disconnect. Sample views and forms are include so it can be easily used. 

It includes:

* A view for the login and one for the logout;
* All the views for the registration request (request, confirmation, etc.);
* A view to ask for the reinitialization of a password;
* Email sending;

In the ``skeleton.html`` template, a partial HTML code is commented. Uncomment it to display the *logout* button when the user is connected.

The registration process consists in sending an email (sender/destination emails have to be configured in settings) with the registration request to an administrator responsible for accepting them (or not). Once validated, an email is sent to the user to confirm his registration by way of a link. Once this step has been completed, the user can connect.

Also, note that this app extend the user model with a profile model. 

This profile is naive because it implement some comon additional fields for sample but you may not need all of them, if you change it you will need to do some changes also in registration view, forms and email senders.

.. note::
   Included forms and templates depends on `crispy_forms`_ mod.

admin_style
-----------

.. _djangocms-admin-style: https://github.com/divio/djangocms-admin-style
.. _django-admin-shortcuts: https://github.com/alesdotio/django-admin-shortcuts/

Enable `djangocms-admin-style`_ to enhance the administration interface. Also enable `django-admin-shortcuts`_.

*admin-style* better fit with DjangoCMS than `admin_tools`_. 

.. warning::
        This mod cannot live with `admin_tools`_, you have to choose only one of them.

admin_tools
-----------

.. _django-admin-tools: https://bitbucket.org/izi/django-admin-tools/

Enable `django-admin-tools`_ to enhance the administration interface. This enables three widgets to customize certain elements and link to `filebrowser`_ module (that should allready be enabled).

.. warning::
        This mod cannot live with `admin_style`_, you have to choose only one of them.

assets
------

.. _django-assets: https://github.com/miracle2k/django-assets/

Enable `django-assets`_ to combine and minify your *assets* (CSS, JS). The minification library used, *yuicompressor*, requires the installation of Java (the OpenJDK installed by default on most Linux systems is sufficient).

In general, this component is required. If you do not intend to use it, you will need to modify the project's default templates to remove all of its occurrences.

Assets are defined in ``project/assets.py`` and some apps can defined their own ``asset.py`` file but our main file does not use them.

Our ``asset.py`` file is divised in three parts :

* BASE BUNDLES: Only for app bundle like Foundation Javascript files or RoyalSlider files;
* MAIN AVAILABLE BUNDLES: Where you defined main bundles for the frontend, use app bundles previously defined;
* ENABLE NEEDED BUNDLE: Bundle you effectively want to use. Bundle that are not defined here will not be reachable from templates and won't be compiled;

autobreadcrumbs
---------------

.. _autobreadcrumbs: https://github.com/sveetch/autobreadcrumbs

Enable `autobreadcrumbs`_ to add automatic breadcrumbs building in templates and applications.

ckeditor
--------

Enable and define customization for the `CKEditor`_ editor. It is enabled by default and used by `Django CKEditor`_ in the `cms`_ mod, and also in `zinnia`_.

Note that DjangoCMS use it's own app named "djangocms_text_ckeditor", a djangocms plugin to use CKEditor (4.x).

But Zinnia (and some other generic app) use "django_ckeditor" that ship the same ckeditor but without cms addons.

This mod contains configuration for all of them.

And some useful patches/fixes :

* the codemirror plugin that is missing from the ckeditor's django apps;
* A system to use the "template" plugin (see views.EditorTemplatesListView for more usage details);
* Some overriding to have content preview and editor more near to Foundation;

cms
---

.. _Django CMS: https://www.django-cms.org/
.. _emencia-cms-snippet: https://github.com/emencia/emencia-cms-snippet

`Django CMS`_ allows for the creation and management of the content pages that constitute your site's tree structure. By default, this component enables the use of `filebrowser`_, `Django CKEditor`_ and `emencia-cms-snippet`_ (a clone of the snippets' plugin with a few improvements).

By default it is configured to use only one language. See its ``urls.py`` to find out how to enable the management of multiple languages.

codemirror
----------

.. _Django Codemirror: https://github.com/sveetch/djangocodemirror

Enable `Django Codemirror`_ to apply the editor with syntax highlighting in your forms (or other content).

It is used by the snippet's CMS plugin.

contact_form
------------

A simple contact form that is more of a standard template than a full-blown application. You can modify it according to your requirements in its ``apps/contact_form/`` directory. Its HTML rendering is managed by `crispy_forms`_ based on a customized layout.

.. note::
   Depends on `recaptcha`_ and `crispy_forms`_ mods.

cookie_law
----------

.. _Emencia Cookie Law: https://github.com/emencia/emencia-cookie-law

To comply to the *European Cookie Law*, `Emencia Cookie Law`_ contain a 
simple kit to easily display a banner about the Cookie law.

You can easily style the banner elements using CSS or even override the 
banner template to fit to the project design.

crispy_forms
------------

.. _Foundation: http://foundation.zurb.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _crispy-forms-foundation: https://github.com/sveetch/crispy-forms-foundation

Enable the use of `django-crispy-forms`_ and `crispy-forms-foundation`_. 

**crispy_forms** is used to manage the HTML rendering of the forms in a finer and easier 
fashion than with the simple Django form API. 

**crispy-forms-foundation** is a supplement to implement the rendering with the structure 
(tags, styles, etc.) used in `Foundation`_.

debug_toolbar
-------------

.. _django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar/

Add `django-debug-toolbar`_ to your project to insert a tab on all of your project's HTML pages, which will allow you to track the information on each page, such as the template generation path, the  query arguments received, the number of SQL queries submitted, etc.

This component can only be used in a development or integration environment and is always disabled during production.

Note that its use extends the response time of your pages and can provokes some bugs (see the warning at end) so for the time being, this mods is disabled. Enable it locally for your needs but never commit its enabled mod and remember trying to disable it when you have a strange bug.

.. warning::
        Never enable this mod before the first database install or a syncdb, else it will result in errors about some table that don't exist (like "django_site").

emencia_utils
-------------

Group together some common and various utilities from ``project.utils``.

filebrowser
-----------

.. _Django Filebrowser: https://github.com/wardi/django-filebrowser-no-grappelli

Add `Django Filebrowser`_ to your project so you can use a centralized interface to manage the uploaded files to be used with other components (`cms`_, `zinnia`_, etc.).

The version used is a special version called *no grappelli* that can be used outside of the *django-grapelli* environment.

Filebrowser manage files with a nice interface to centralize them and also manage image resizing versions (original, small, medium, etc..), you can edit these versions or add new ones in the settings.

.. note::
        Don't try to use other resizing app like sorl-thumbnails or easy-thumbnails, they will not work with Image fields managed with Filebrowser.

filer
-----

.. _django-filer: https://github.com/stefanfoulis/django-filer

Mod for `django-filer`_ and its DjangoCMS plugin

Only enable it for specific usage because this can painful to manage files with Filebrowser and django-filer enabled in the same project.

flatpages
---------

.. _Django flatpages app: https://docs.djangoproject.com/en/1.5/ref/contrib/flatpages/

Enable the use of `Django flatpages app`_ in your project. Once it has been enabled, go 
to the ``urls.py`` in this mod to configure the *map* of the urls to be used.

google_tools
------------

.. _django-google-tools: https://pypi.python.org/pypi/django-google-tools

Add `django-google-tools`_ to your project to manage the tags for *Google Analytics* and *Google Site Verification* from the site administration location.

.. note::
        The project is filled with a custom template ``project/templates/googletools/analytics_code.html`` to use Google Universal Analytics, remove it to return to the old Google Analytics.

icomoon
-------

.. _Django Icomoon: https://github.com/sveetch/django-icomoon

`Django Icomoon`_ help you to manage your webfonts with Icomoon service. It won't work with a webfont not generated on Icomoon site because it depends on a JSON manifest file (you could make it yourself but it's a little bit complicated).

This mod can handle many webfonts if you need, you just have to define them in the mod settings, at least one webfont is required.

Once one or more webfonts are defined, `Django Icomoon`_ can help you to automatically deploy them in your project from downloaded Zip on Icomoon using a command line ``django-instance icomoon_deploy``.

Also when deployed and the webfonts are loaded in your templates, you can visualize every icons from a gallery located at ``/icomoon/``.

logentry
--------

.. _django-logentry-admin: https://github.com/yprez/django-logentry-admin

Enable `django-logentry-admin`_ to browse all admin log entries at contrary to default Django admin behavior that only display the last entries.

pdb
---

.. _pip: http://www.pip-installer.org
.. _Django PDB: https://github.com/tomchristie/django-pdb

Add `Django PDB`_ to your project for more precise debugging with breakpoints. 

N.B. Neither ``django_pdb`` nor ``pdb`` are installed by buildout. You must install 
them manually, for example with `pip`_, in your development environment so you do not 
disrupt the installation of projects being integrated or in production. You must also 
add the required breakpoints yourself.

See the the django-pdb Readme for more usage details.

.. note::
        Make sure to put django_pdb after any conflicting apps in INSTALLED_APPS so 
        that they have priority.
        
        So with the automatic loading system for the mods, you should enable it with a 
        name like "zpdb", to ensure that it is loaded at the end of the loading loop.

porticus
--------

.. _Django Porticus: https://github.com/emencia/porticus
.. _DjangoCMS plugin for Porticus: https://github.com/emencia/cmsplugin-porticus

Add `Django Porticus`_ to your project to manage file galleries.

There is a `DjangoCMS plugin for Porticus`_, it is not enabled by default, you will have to uncomment it in the mod settings.

recaptcha
---------

.. _Service reCaptcha: http://www.google.com/recaptcha

Enable the `Django reCaptcha`_ module to integrate a field of the *captcha* type via the `Service reCaptcha`_. This integration uses a special template and CSS to make it *responsive*.

.. note::
   If you do in fact use this module, go to its mods setting file (or that of your environment) to fill in the public key and the private key to be used to transmit the data required.

   By default, these keys are filled in with a *fake* value and the captcha's form field therefore sends back a silent error (a message is inserted into the form without creating a Python *Exception*).

sendfile
--------

.. _django-sendfile: https://github.com/johnsensible/django-sendfile

Enable `django-sendfile`_ that is somewhat like a helper around the **X-SENDFILE headers**, a technic to process some requests before let them pass to the webserver.

Commonly used to check for permissions rights to download some private files before let the webserver to process the request. So the webapp can execute some code on a request without to carry the file to download (than could be a big issue with some very big files).

`django-sendfile`_ dependancy in the buildout config is commented by default, so first you will need to uncomment its line to install it, before enabling the mod. Then you will need to create the directory to store the protected medias, because if you store them in the common media directory, they will public to everyone.

This directory must be in the project directory, then its name can defined in the ``PROTECTED_MEDIAS_DIRNAME`` mod setting, default is to use ``protected_medias`` and so you should create the ``project/protected_medias`` directory.

**Your webserver need to support this technic**, no matter on a recent nginx as it is allready embeded in, on Apache you will need to install the Apache module XSendfile (it should be availabe on your distribution packages) and enable it in the virtualhost config (or the global one if you want), see the `Apache module documentation <https://tn123.org/mod_xsendfile/>`_ for more details. Then remember to update your virtualhost config with the needed directive, use the Apache config file builded from buildout.

The nginx config template allready embed a rule to manage ``project/protected_medias`` with sendfile, but it is commented by default, so you will need to uncomment it before to launch buildout again to build the nginx config file.

.. note::
        By default, the mod use the django-sendfile's backend for development that is named ``sendfile.backends.development``. For production, you will need to use the right backend for your webserver (like ``sendfile.backends.nginx``).

Finally you will need to implement it in your code as this will require a custom view to download the file, see the `django-sendfile`_  documentation for details about this. But this is almost easy, you just need to use the ``sendfile.sendfile`` method to return the right Response within your view.

site_metas
----------

.. _Django sites app: https://docs.djangoproject.com/en/1.5/ref/contrib/sites/

Enable a module in ``settings.TEMPLATE_CONTEXT_PROCESSORS`` to show a few variables linked to `Django sites app`_ in the context of the project views template.

Common context available variables are:

* ``SITE.name``: Current *Site* entry name;
* ``SITE.domain``: Current *Site* entry domain;
* ``SITE.web_url``: The Current *Site* entry domain prefixed with the http protocol like ``http://mydomain.com``. If HTTPS is enabled 'https' will be used instead of 'http';

Some projects can change this to add some other variables, you can see for them in ``project.utils.context_processors.get_site_metas``.

sitemap
-------

.. _Sitemap framework: https://docs.djangoproject.com/en/1.5/ref/contrib/sitemaps/

This mod use the Django's `Sitemap framework`_ to publish the ``sitemap.xml`` for various apps. The default config contains ressources for DjangoCMS, Zinnia, staticpages, contact form and Porticus but only ressource for DjangoCMS is enabled.

Uncomment ressources or add new app ressources for your needs (see the Django documentation for more details).

slideshows
----------

.. _emencia-django-slideshows: https://github.com/emencia/emencia-django-slideshows

Enable the `emencia-django-slideshows`_ app to manage slide animations (slider, carousel, etc.). This was initially provided for *Foundation Orbit* and *Royal Slider*, but can be used with other libraries if needed.

staticpages
-----------

.. _emencia-django-staticpages: https://github.com/emencia/emencia-django-staticpages

This mod uses `emencia-django-staticpages`_ to use static pages with a direct to template process, it replace the deprecated mod *prototype*.

thumbnails
----------

.. _easy-thumbnails: https://github.com/SmileyChris/easy-thumbnails/

Mod for `easy-thumbnails`_ a library to help for making thumbnails on the fly (or not).

Generally **this is not recommended**, because by default we allready enable Filebrowser that allready ships a `thumbnail system <http://django-filebrowser.readthedocs.org/en/latest/versions.html>`_.

urlsmap
-------

.. _django-urls-map: https://github.com/sveetch/django-urls-map

`django-urls-map`_ is a tiny Django app to embed a simple management command that will display the url map of your project.

xiti
----

.. _Django-xiti: https://github.com/emencia/django-xiti

Mod to define `Django-xiti`_ settings to load Xiti HTML code into templates

Since Xiti usage is not common, this mod is not installed or enabled on default install, you will need to enable it's egg in buildout, enable its mod and finally update ``marketing_tags.html``  to load it.

zinnia
------

.. _Django Blog Zinnia: https://github.com/Fantomas42/django-blog-zinnia

`Django Blog Zinnia`_ allows for the management of a blog in your project. It is well integrated into the `cms`_ component but can also be used independently.



