.. Never edit this file manually, instead edit its template in
   'templates/project_structure.rst' and use 'make grab' to build
   with mods documentations

.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Foundation: http://foundation.zurb.com/
.. _Compass: http://compass-style.org/
.. _Boussole: http://boussole.readthedocs.io/
.. _SCSS: http://sass-lang.com/
.. _SASS: http://sass-lang.com/
.. _Bourbon: http://bourbon.io/
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

Aim is to never commit files created from buildout (installed packages, app development sources, etc..), compiled static files, project media files and database.

Makefile
********

Project embeds a ``Makefile`` file that contains some usefull commands to build your project.

``install``
    to proceed to a new install of this project. Use clean command before if you want to reset a current install
``install-dev``
    to proceed to a new install of this project with additional sources for development
``install-foundation``
    to install (or re-install) Foundation sources
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

SASS
****

Produced project contain a `SASS`_ structure ready to use and contains `Foundation`_ and `Bourbon`_ libraries.

Included HTML templates was done using `Foundation`_, so you will need to change them if you plan to use another SASS framework.

SASS sources and libraries are compatible with any compiler which implement SASS >= 3.2.x references.

We strongly advise you to use `Boussole`_ to avoid messing with some Ruby or Node.js installation. `Compass`_ 1.x is still supported. In the SASS sources directory a default configuration is available for both of them.

.. WARNING::
   Compass was not only a compiler, it include also some SASS framework we were using. It's most important feature was *vendor prefix* for many CSS3 properties but this is not needed for almost all of them.

   If you use Compass, **never use any Compass mixin or stuff** in your SASS sources, it will break compatibility people using Boussole.

   For CSS3 properties requiring vendor prefix, we include `Bourbon`_ framework instead. If you are not sure about vendor prefix needs, search in `Can I Use <http://caniuse.com/>`_ database.


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

.. _available_mods:

Available mods
**************

.. document-mods::