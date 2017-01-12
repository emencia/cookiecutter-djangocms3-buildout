.. _emencia_paste_djangocms_3: https://github.com/emencia/emencia_paste_djangocms_3
.. _jquery-smartresize: https://github.com/louisremi/jquery-smartresize
.. _googleclosure: https://developers.google.com/closure/compiler/

History
=======

Versions come from git tags.

Version 1.7.0 - Unreleased
--------------------------

* fix new pep error E305
* exclude migrations folder from flake8 check
* use same ssl certification folder on dev host
* add fabric script for install/deploy production version
* add CHANGELOG file and build first release number with jinja2-time
* use a .flake8 file for flake8 settings
* fix bug in __init__.py generation that added trailing whitespace

Version 1.6.0 - 2016/12/17
--------------------------

* Now require ``cookiecutter==1.4.0`` (although for now this should not break for >=1.1.0,<1.4.0);
* Fixed typo on ``secret_key`` template part in ``cookiecutter.json``, close #73;
* Updated project Readme;
* Updated install documentation about required devel libraries;
* Upgraded to ``django==1.8.17``;

Version 1.5.0 - 2016/11/29
--------------------------

* Added files to use Continuous Integration (*CI*) with Jenkins/Fabric;
* Cleaned code with flake8 and add a rule to run flake8 into Makefile;
* Added ``django-datadownloader``;
* Added initial migration for ``project.contact_form``;
* Upgraded to ``django==1.8.16``, close #72;

Version 1.4.4 - 2016/10/06
--------------------------

* Upgraded to ``django==1.8.15``, close #68;
* Fixed icomoon mod settings for ``sass`` dir new path, close #69;
* Upgraded to ``django-debug-toolbar==1.5`` to fix a bug with sqlquery panel, close #70
* Added makefile action ``livehtml`` for ``sphinx-autobuild`` usage (have to install it before, not in dependancies);
* Added new settings ``MARKETINGTAGS_ENABLED`` (default value depend on ``DEBUG`` setting) to determine marketing tags display from ``skeleton.html``. Also added an additional context processor to expose this setting to default template context, close #71;

Version 1.4.3 - 2016/09/24
--------------------------

* Fix minor typo on CookieConsent message quotes, close #66;
* Disabled ``PO-Projects-client`` egg and buildout part again since nap is breaked, close #67;
* Upgraded to ``django-assets==0.12``;

Version 1.4.2 - 2016/09/04
--------------------------

* Removed ``emencia-cookie-law`` in profit of a Javascript library `Cookie Consent <https://silktide.com/tools/cookie-consent/>`_ which works better with webapp caches;
* Fixed ``js/jquery/button-dropdown-trick.js`` which contained unecessary Foundation init;

Version 1.4.1 - 2016/08/20
--------------------------

* Fixed ``cookiecutter.json`` so the settings files are rendered correctly with Jinja variable from cookiecutter during project generation, close #64;

Version 1.4.0 - 2016/08/05
--------------------------

* Upgraded to ``django==1.8.14``, close #63;
* Upgraded to ``django-google-tools==1.1.0``, close #60;
* Enable ``mptt`` through Zinnia settings, so we can use ``recursetree`` tag in ``categorie_tree.html`` zinnia template, close #57;
* Restore ``PO-Projects-client`` installation, close #62;
* Add some Javascript code in ``app.js`` to implement clickable slider from ``emencia-django-slideshows``, close #58;
* Added a template ``pagination.html`` for paginate object with generic class based view ``ViewList``;

Version 1.3.0 - 2016/06/12
--------------------------

* Added usage of `googleclosure`_ for Javascript minification instead of ``yuicompressor`` (caused many issues with recent scripts because yui is not maintained anymore against recent Ecmascript versions). Related to issue #50;

    * ``closure`` is installed through a Python meta package alike ``yuicompressor``;
    * ``yuicompressor`` is still used for CSS minification until we find something as stable;
    * Added Makefile action ``delminifiedassets`` to clean previous minified files from leading assets bundles;

* Added a note about `Ckeditor configurable sanitizer <https://github.com/divio/djangocms-text-ckeditor#configurable-sanitizer>`_ in its mod settings. Related to issue #46;

Version 1.2.2 - 2016/05/29
--------------------------

* Freezed to ``djangocms-text-ckeditor==2.9.3``, close #55;
* Upgraded to ``porticus==1.1.0``, close #54;
* Upgraded to ``cmsplugin-porticus==0.4.1``, close #54;
* Upgraded to ``cmsplugin-zinnia==0.8.1``, close #53;
* Added "CurrentMediaQuery" plugin and enable it only when Django debug mode is on;

Version 1.2.1 - 2016/05/17
--------------------------

* Dropped assets (Javascript, SASS and CSS) for RoyalSlider, Masonry and MMenu since they are not really used anymore;
* Changed ``sass/scss/addons/_type.scss`` to override Foundation types for titles instead of using extend;
* Close #48:

  * Cleaning ``js/app.js``: removed unused code, moved sample plugins code to their own file within ``js/jquery/``;
  * Fix broken Ckeditor within cms text plugin introduced since Image-swapper plugin has been moved to its own file (``js/jquery/jquery.image-swapper.js``);

Version 1.2.0 - 2016/05/02
--------------------------

Move to full libsass support but stay compatible with "Compass 1.x".

This is related to issue #43

* Moved ``compass`` directory to ``sass`` directory with a new structure;

    * Divided addons files;
    * Added Bourbon 4.2.6;
    * Foundation5 SASS sources now lives in sass directory;
    * Keep a config file for Compass support;

* Removed Foundation5 sources directory, now we only ship SASS and Javascripts sources in their respective location;
* Updated Makefile action ``syncf5`` to synchronize SASS sources to the ``sass`` directory;
* flags stylesheet is not supported for now because it stand Compass sprites;
* admin_styles stylesheet is not supported for now;
* Updated documentation;
* Dropped ``admin_tools`` mod that is not supported anymore;
* Fixed a bug with a wrong import path for icomoon fonts;
* Upgrade to django-icomoon 0.4.0, close #47;

Version 1.1.1 - 2016/05/02
--------------------------

* Add option to use https within nginx conf;

Version 1.1.0 - 2016/04/19
--------------------------

* Upgraded to ``django==1.8.12``;
* Upgraded to ``django-icomoon==0.4.0``;
* Upgraded to ``django-xiti==0.1.1``;


Version 1.0.0 - 2016/03/19
--------------------------

* Upgraded dependencies versions for upgrade to ``Django==1.8``;

    * ``django==1.8.11``;
    * ``psycopg2==2.6.1``;
    * ``Pillow==3.1.1``;
    * ``django-mptt==0.7.4``;
    * ``django-cms==3.2.3``;
    * ``django-registration-redux==1.4``;
    * ``djangocms-admin-style==1.1.0``;
    * ``django-admin-tools==0.7.2``;
    * ``django-filebrowser-no-grappelli==3.6.1``;
    * ``django-assets==0.11``;
    * ``django-recaptcha==1.0.5``;
    * ``django-debug-toolbar==1.4``;
    * ``django-extensions==1.6.1``;
    * ``django-filer==1.1.1``;
    * ``cmsplugin-filer==1.0.1``;
    * ``django-icomoon==0.3.1``;
    * ``django-sendfile==0.3.10``;
    * ``easy-thumbnails==1.5``;
    * ``django-contrib-comments==1.6.2``;
    * ``django-blog-zinnia==0.16``;
    * ``django-tagging==0.4.1``;
    * ``django-taggit==0.18.0``;
    * ``sorl-thumbnail==12.2``;

* Removed all occurences to ``socialaggregator`` that is not supported anymore;
* Updated project settings and mods settings to use the new ``TEMPLATE`` setting that contain all template backends settings;
* Added empty ``TEXT_ADDITIONAL_ATTRIBUTES`` setting for ckeditor;
* Some minor changes and cleaning in mods settings;
* Added mod for ``autobreadcrumbs``;
* Updated ``djangocms_admin_style`` Sass and CSS stylesheets to the app version 1.1.0;
* Patched them for Filebrowser and also for a bug regression with libsass 3.3.3;
* Although these Sass stylesheets are in compass directory, they can only be compiled with libsass;
* Upgraded to ``django-crispy-forms==1.6.0`` to remove some warnings from django checks;

Version 0.9.3 - 2015/12/19
--------------------------

* Upgraded to ``django-cms==3.1.4``;
* Upgraded to ``django-admin-shortcuts==1.2.6``;
* Upgraded to ``djangocms-admin-style==0.2.8``;
* Updated ``djangocms-admin-style`` SCSS source and recompile them again, it should definitively close issue #39;
* Removed ``compass/Gemfile`` because it cause too many issues when switching between rvm gemset (like to compile the main scss then the admin one);

Version 0.9.2 - 2015/12/17
--------------------------

**Upgrade to buildout 2.5.0** and dependancies:

* Removed ``bootstrap.py``, now we just install buildout throught pip;
* Upgraded to ``setuptools>=19.1``;
* Upgraded to ``pip>=7.1.2``;
* Upgraded to ``buildout==2.5.0``, close #41;
* Upgraded to ``zc.recipe.egg==2.0.3``;
* Upgraded to ``buildout.recipe.uwsgi==0.1.1``;
* Upgraded to ``collective.recipe.cmd==0.11``;
* Upgraded to ``collective.recipe.template==1.13``;
* Upgraded to ``djangorecipe==2.1.2``;
* Updated Makefile ``install`` action for theses changes;
* Updated ``[uwsgi]`` buildout part since ``buildout.recipe.uwsgi==0.1.1`` deprecate option prefix ``xml-`` in profit of ``config-``;
* Added ``pip-selfcheck.json``, ``gestus.cfg`` and ``po_projects.cfg`` to Makefile ``clean`` action;

For now we are relaxing again ``setuptools`` and ``pip`` to a knowed working version or better. We may fix a version again in future if we encounter some bug.

Version 0.9.1 - 2015/12/13
--------------------------

* Added Javascript library `jquery-smartresize`_ for **Debounced and Throttled Resize Events for jQuery**. Not enabled by default. This close #42;

Version 0.9.0 - 2015/12/13
--------------------------

Goal of this version was to port structure, code and components to ``Django==1.7``.

Many Django apps have been upgraded and some mods settings have been updated.

There is too much changes to write them all here, see the dedicated document :ref:`Porting to Django 1.7 history <def-history-port-django17>` for full details.

Version 0.8.2 - 2015/10/30
--------------------------

* Fixed usage of template context variable for ``DEBUG`` setting, seems it's not exposed in context as uppercase since a long time (if even been), it's lowercase now;
* Fixed Ckeditor custom ``styles.js`` not loaded from mod, close #35;
* Use staticfiles template tag instead of STATIC_URL in our shipped templates, close #36;
* Fixed wrong gitignore that caused uncommited foundation5 sources when pushing created new projects to their repository (will need to watch for this gignore changes when eventually update foundation sources from last their version), close #38;
* Updated to ``emencia-cookie-law==0.2.3``;
* Added ``django-xiti==0.1.0`` structure (template, mod, etc..) but not installed or enabled on defaut install;

Version 0.8.1 - 2015/10/22
--------------------------

* Fixed missing ``__init__.py`` in ``project/utils/templatetags``, close #34;
* Update to ``zinnia-wysiwyg-ckeditor==1.2`` to get rid of ``django-ckeditor-updated`` dependancy and now stands only on ``django-ckeditor``. Note that we don't go to ``zinnia-wysiwyg-ckeditor==1.3`` because it depends on ``django-ckeditor=5.x`` that we didn't audit yet;

Version 0.8.0 - 2015/10/18
--------------------------

* Updated Foundation to ``5.5.3`` version, this require now Compass 1.x install to compile, close #22;
* Updated Makefile for some Foundation install strategy changes;
* Updated SCSS to fit to Foundation changes;
* Updated to ``django-icomoon==0.3.0``;
* Updated documentation for new methodology with webfont since ``django-icomoon`` usage;

Version 0.7.6 - 2015/10/01
--------------------------

* Added and enabled mod for ``emencia-cookie-law``, close #32;
* Added and enabled mod for ``django-icomoon``, close #31;
* Updated documentation, close #33
* Fixed ``django-crispy-forms`` mod settings for last release, updated to ``crispy-forms-foundation==0.5.3``, #29;
* Added ``reload`` action to the Makefile, to restart the uwsgi instance on integration or production environment;


Version 0.7.3 - 2015/08/31
--------------------------

* Updated docs to add tips about *RVM Gemsets*;
* Fixed ``django-reversion==1.8.7`` for issue #27;
* Fixed *sitemap* mod ``urls.py``, close #28;


Version 0.7.2 - 2015/06/13
--------------------------

* Added some cleaning when using 'make assets' command;
* Updated some scss, Enabled default icomoon webfont;
* Updated some docs;

Version 0.7.1 - 2015/06/06
--------------------------

* Fix some included html templates to use ``<h1>`` instead of ``<h2>``, although Django apps templates probably all use ``<h2>`` again, so we will need to override them;

Version 0.7.0 - 2015/06/06
--------------------------

* Use ``fonts_dir`` setting in compass config, close #13
* Use *lazy protocole prefix* to load googlefont, close #12;
* Remove ``<h1>`` usage in topbar for a better semantic (``<h1>`` should not be identical to ``<title>``), **WARNING: now all cms page must define their own h1, also other app template have to define the right h1**;
* Get back our CMS snippet plugin, temporary using our fork as a develop source, close #19;
* Upgrade ``django-admin-style`` to ``0.2.7``, close #18;
* Fix to ``djangocms_text_ckeditor==2.4.3``, close #16;
* Include Slick.js, close #17;
* Remove Foundation Orbit usage because it is deprecated and Slick.js works better;
* ``project/assets.py`` is now processed by cookiecutter+Jinja so we can disable assets from user choices like for socialaggregator Javascript library;
* Reorganize SCSS sources:

  * ``components/`` directory is for page parts or specific Django apps layout;
  * ``vendor/`` directory contains all SCSS for included library (like mmenu, royalslider, etc..);
  * ``utils/`` directory contains all utils stuff like mixins, basic addons, Foundation patches, etc..;
  * Added Flexbox support;

* Remove interchange template for slideshows;
* Cleaning ``app.js`` since Orbit is not used anymore;

Version 0.6.6 - 2015/05/16
--------------------------

* Enforce ``django-tagging==0.3.4`` (to avoid a bug with django<=1.7);
* Review and update ``assets.py``, close #10;
* Some assets cleanup, close #9;

  * Added missing default images for *Royal Slider*;
  * Removed Foundation3 Javascript stuff;
  * Cleaning main frontend script ``app.js``;
  * Added MegaMenu stuff;

* Big update on ``contact_form`` app:

  * Fix print message on template;
  * Reorganise admin view;
  * Use ``django-import-export`` for exporting contact datas;
  * Don't print captcha on form when ``settings.DEBUG`` is ``True``;

Version 0.6.5 - 2015/05/03
--------------------------

* Cleaning documentations;
* Restored doc stuff to automatically build mod documentations;
* Updated to ``django-cms==3.0.13``;
* Enforce ``django-contrib-comments==1.5.0`` (to avoid a bug with django<=1.7);
* Integrated ``django-logentry-admin`` as a default enabled mod, close #8;
* Fixed doc config to get the right version number from git tags;

Version 0.6.1 - 2015/04/20
--------------------------

* Added cookiecutter context in ``project/__init__.py`` file;

Version 0.6.0 - 2015/04/19
--------------------------

* Better documentation;

Version 0.5.0 - 2015/04/17
--------------------------

* Enabled cms translation and some settings from cookiecutter context, close #4;

Version 0.4.0 - 2015/04/16
--------------------------

* Removed unused variables in ``cookiecutter.json``;
* Changed ignored files from jinja to target some files to use as templates;
* Changed template for ``skeleton.html`` to remove occurences to not enabled apps;
* Added cookiecutter context usage to remove unused sitemap parts, close #5;
* Changed buildout.cfg to be more flexible without some enabled apps;

Version 0.3.0 - 2015/04/15
--------------------------

* Added Git repo initialization in the post generation hook;
* Added a message at the end of the post generation hook to display some help;
* Changed some variables from ``cookiecutter.json`` for repository infos;

Version 0.2.0 - 2015/04/13
--------------------------

* Added post generation hook to enable mods after install;
* Use cookiecutter context to remove eggs in ``buildout.cfg`` egg list;

Version 0.1.0 - 2015/04/12
--------------------------

* First version started from `emencia_paste_djangocms_3`_ structure version ``1.4.0``;
* Not ready to be used yet, it misses some things for now;
