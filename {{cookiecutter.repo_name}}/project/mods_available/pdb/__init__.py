"""
Add `Django PDB`_ to your project for more precise debugging with breakpoints. 

N.B. Neither ``django_pdb`` nor ``pdb`` are installed by the buildout. You must install 
them manually, for example with `pip`_, in your development environment so you do not 
disrupt the installation of projects being integrated or in production. You must also 
add the required breakpoints yourself.

See the the django-pdb Readme for more usage details.

.. note::
        django-pdb should be put at the end of settings.INSTALLED_APPS :
        
        "Make sure to put django_pdb after any conflicting apps in INSTALLED_APPS so 
        that they have priority."
        
        So with the automatic loading system for the mods, you should enable it with a 
        name like "zpdb", to assure that it is loaded at the end of the loading loop.
"""