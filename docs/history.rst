.. _emencia_paste_djangocms_3: https://github.com/emencia/emencia_paste_djangocms_3

History
=======

Versions come from git tags, not package version because, err.. this is not a Python package.

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
