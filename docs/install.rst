.. _virtualenv: http://www.virtualenv.org/
.. _buildout: http://www.buildout.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Epaster: https://github.com/emencia/Epaster

=======
Install
=======

There is no need to install anything but `Cookiecutter`_, when it's done you can use any `Cookiecutter`_ templates directly from a repository (local, hosted on github, etc..): ::

    pip install cookiecutter

It's done.

Created projects requirements
*****************************

.. NOTE::
   If you allready have installed `Epaster`_, don't worry about this part.

Although the template itself don't need anything but `Cookiecutter`_, a project created with this template will requires some libraries to build it and use it:

* `virtualenv`_;
* Python development library (commonly known as ``python-devel``);
* ``libjpeg``;
* ``zlib``;
* ``libfreetype``;

The method to install them depends on your plateform :

* On **Linux** systems you will install them with your package system like ``apt-get``, see `Pillow documentation for Linux <http://pillow.readthedocs.org/en/latest/installation.html#linux-installation>`_;
* On **MacOSX**, the recommended way is to use ``brew`` utility, see `Pillow documentation for OSX <http://pillow.readthedocs.org/en/latest/installation.html#os-x-installation>`_;
* **Windows** system is not supported, you probably can install needed stuff but with some works on your own;

Also if you need to use a **PostgreSQL** database instead of the default **sqlite3** database, you will need a library to build **psycopg2**, this library is called ``libpq``.

.. NOTE::
   All created projects are shipped with a README file that contain all necessary details to build it and use it. This will be a simplified procedure with a **Makefile** command to launch the `buildout`_ process.
