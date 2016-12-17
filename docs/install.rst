.. _pip: https://pip.pypa.io/
.. _virtualenv: http://www.virtualenv.org/
.. _buildout: http://www.buildout.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter

=======
Install
=======

There is no need to install anything but `Cookiecutter`_, when it's done you can use any `Cookiecutter`_ templates directly from a repository (local, hosted on github, etc..): ::

    pip install cookiecutter

It's done.

Created projects requirements
*****************************

Although the project template don't need anything but `Cookiecutter`_, a created project will requires `pip`_, `virtualenv`_ and some libraries to install it.

There is the **required Basic** development libraries and some optional other ones for some tasks. Note that package name can differ depending from your system.

Basic
    * ``python-dev``;
    * ``gettext``;
    * ``gcc``;
    * ``make``;
    * ``libjpeg``;
    * ``zlib``;
    * ``libfreetype``;

For Postgresql driver (psycopg2)
    * ``libpq``;

For Mysql driver
    * ``libmysqlclient-dev``;

For M2Crypto
    * ``swig``;

For Graphviz
    * ``graphviz``;
    * ``libgraphviz-dev``;
    * ``graphviz-dev``;

The method to install system packages depends on your plateform:

* On **Linux** systems you will install them with your package system like ``apt``, see `Pillow documentation for Linux <http://pillow.readthedocs.org/en/latest/installation.html#linux-installation>`_;
* On **MacOSX**, the recommended way is to use ``brew`` utility, see `Pillow documentation for OSX <http://pillow.readthedocs.org/en/latest/installation.html#os-x-installation>`_;
* **Windows** system is not supported, you probably can install needed stuff but with some works on your own;

.. NOTE::
   All created projects are shipped with a README file that should contains all necessary details to build it and use it. This will be a simplified procedure with a **Makefile** command to launch the `buildout`_ process.
