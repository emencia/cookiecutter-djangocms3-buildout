.. cookiecutter-djangocms3-buildout documentation master file, created by
   sphinx-quickstart on Fri Apr 17 04:03:41 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _Emencia: http://www.emencia.com/
.. _virtualenv: http://www.virtualenv.org/
.. _buildout: http://www.buildout.org/
.. _Django: https://www.djangoproject.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Django CMS: https://www.django-cms.org/
.. _Django Blog Zinnia: https://github.com/Fantomas42/django-blog-zinnia
.. _Django CKEditor: https://github.com/divio/djangocms-text-ckeditor/
.. _Django Filebrowser: https://github.com/wardi/django-filebrowser-no-grappelli
.. _SASS: http://sass-lang.com/
.. _Foundation: http://foundation.zurb.com/
.. _Bourbon: http://bourbon.io/
.. _uwsgi: https://uwsgi-docs.readthedocs.io
.. _nginx: https://www.nginx.com/
.. _monit: https://mmonit.com/monit/

cookiecutter-djangocms3-buildout
================================

A `Cookiecutter`_ template to produce a structure for a `Django CMS`_ project.

Features
********

* Many Django apps pre-configured and ready to work (see :ref:`available_mods`);
* Django project is based on:

  * `Django CMS`_;
  * `Django Blog Zinnia`_;
  * `Django CKEditor`_;
  * And many other... All of them are allready configured and ready to work;

* `buildout`_ ensure deployment on various environments;
* Web design integration is made with `SASS`_ (>=3.2.x) using libraries `Foundation`_ and `Bourbon`_;
* Some pre configuration are ready for `uwsgi`_, `nginx`_ and `monit`_;

`Emencia`_ company uses this tool for web projects along with our techniques and procedures.

Goal is to automatically create and initialize a complete project structure so you don't lose time assembling all parts and components.

Table of contents
*****************

.. toctree::
   :maxdepth: 2

   install.rst
   usage.rst
   project_structure.rst
   topics.rst
   history.rst
