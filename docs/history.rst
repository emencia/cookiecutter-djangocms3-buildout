.. _emencia_paste_djangocms_3: https://github.com/emencia/emencia_paste_djangocms_3

History
=======

Versions come from git tags, not package version because, err.. this is not a Python package.

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
