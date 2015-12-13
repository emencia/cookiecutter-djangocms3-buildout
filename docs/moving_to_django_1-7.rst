
.. _def-history-port-django17:

=============================
Porting to Django 1.7 history
=============================

This document relates all steps done to move this cookiecutter template from **0.8.2** (``Django==1.6``) to 0.9.0 (``Django==1.7``).

Version 0.9.0 Pre-release 7 - 2015/12/13
----------------------------------------

* Upgraded to ``django-registration==1.2`` and enable it;
* Refurbished ``project.accounts`` so it's compatible with ``django-registration==1.2`` and cleaner;
* Enable again the ``accounts`` mod;
* This is the last pre release since all components have been proudly ported to ``Django>=1.7``;

Version 0.9.0 Pre-release 6 - 2015/12/11
----------------------------------------

* Don't use our ``djangocms-snippet`` fork anymore, instead use the legacy egg in last version ``1.7.1``;
* Upgraded to ``django-import-export==0.4.0`` and enable it;
* Upgraded to ``django-recaptcha==1.0.4`` and enable it;
* Upgraded to ``emencia.django.countries==0.2.2`` and enable it;
* Enable again the ``contact_form`` mod;
* Now use new system 'NoCaptcha ReCaptcha' in ``recaptcha`` mod;
* Add deprecation message in ``socialaggregator`` mod;
* Fixed ``cms`` mod: changed middleware path from ``django.middleware.doc.XViewMiddleware`` to ``django.contrib.admindocs.middleware.XViewMiddleware`` to avoid deprecation warning;

Version 0.9.0 Pre-release 5 - 2015/11/29
----------------------------------------

* Enabled ``djangocms-snippet`` since it has been correctly ported to ``django==1.7.x``. Note that the port result in incompatible migrations and models states with our previous fork snippet;

Version 0.9.0 Pre-release 4 - 2015/11/28
----------------------------------------

* Upgraded to ``django==1.7.11`` for last security release;
* Upgraded to ``emencia-django-slideshows==1.0.0`` and enable its mod;
* Added ``cmsplugin-slideshows==0.1.0``;

Version 0.9.0 Pre-release 3 - 2015/11/08
----------------------------------------

* Enabled again ``cmsplugin-porticus`` with Django 1.7 support;
* Upgraded to ``cmsplugin-porticus==0.3`` and enable it;
* Upgraded to ``django-cms==3.1.3``;

Version 0.9.0 Pre-release 2 - 2015/11/08
----------------------------------------

* Upgraded to ``porticus==1.0.1`` and enable its mod;
* Upgraded to ``django-filebrowser-no-grappelli==3.5.8``;

Version 0.9.0 Pre-release 1 - 2015/11/01
----------------------------------------

This started with version ``0.8.2`` (well in fact some commits ahead this version, but strictly just before the first pre-release).

From this pre-release: the buildout project install, Django run, CMS and Zinnia works. Still have all disabled apps to return to life.

* Disabled many eggs and mods, just keeping DjangoCMS base stuff and knowed apps as compatible >= 1.7;
* Makefile changes:

  * Added ``django-instance createsuperuser`` at the end of ``install`` action since ``syncdb`` is deprecated and migrations won't prompt for this;
  
* Buildout changes:
  
  * Removed ``south`` egg;
  * Disabled eggs ``porticus``, ``emencia-django-slideshows``, ``emencia-django-socialaggregator`` and their dependancy egg versions;
  * Disabled fixed version for egg ``djangocms-text-ckeditor``, ``djangocms-snippet``, ``django-tagging``, ``django-contrib-comments``;
  * Upgraded egg ``django`` to ``1.7.10``;
  * Upgraded egg ``djangorecipe`` to ``2.1.1``;
  * Upgraded egg ``django-cms`` to ``3.1.2``;
  * Upgraded egg ``psycopg2`` to ``2.5.5``;
  * Upgraded egg ``django-blog-zinnia`` to ``0.15.2``;
  * Upgraded egg ``cmsplugin-zinnia`` to ``0.8``;

* Settings changes:

  * Disabled our djangocms-snippet fork, using legacy apps until our own has evolved for compatibility;
  * Added ``MIGRATION_MODULES``, to ensure migrations (South/Django) compatibility with some apps;
  * Added ``BASE_DIR`` a new common setting for Django;
  * Removed ``STATICFILES_FINDERS`` and ``TEMPLATE_LOADERS`` because default Django value is the same we used and no mod seems requiring them;
  * Always enable ``django.middleware.locale.LocaleMiddleware`` (seems required from Django CMS);

* Urls.py changes:

  * Removed ``admin.autodiscover()`` because now Django admin is allready enabled by default;

* Updated ``wsgi.py`` (almost the same, mostly for comments);
* Fixed default zinnia templates to load tag library ``zinnia`` instead of old name ``zinnia_tags``;
