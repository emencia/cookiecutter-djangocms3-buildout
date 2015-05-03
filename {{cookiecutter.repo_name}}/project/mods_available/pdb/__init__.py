"""
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
"""