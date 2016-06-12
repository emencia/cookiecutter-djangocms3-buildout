"""
.. _django-assets: https://github.com/miracle2k/django-assets/
.. _yuicompressor: http://yui.github.io/yuicompressor/
.. _googleclosure: https://developers.google.com/closure/compiler/

Enable `django-assets`_ to combine and minify your *assets* (CSS, JS).

There are two used minification libraries:

* `yuicompressor`_ for CSS;
* `googleclosure`_ for Javascript;

Both of them requires the installation of Java (OpenJDK installed on most Linux systems is sufficient), they are installed through some Python meta package from Pypi.

In general, this mod is required. If you do not intend to use it, you will need to modify the project's default templates to remove all of its occurrences.

Assets are defined in ``project/assets.py`` and some apps can defined their own ``asset.py`` file but our main file does not use them.

Our ``assets.py`` file is divised in three parts :

* BASE BUNDLES: Only for app bundle like Foundation Javascript files, Modernizr files, etc..;
* MAIN AVAILABLE BUNDLES: Where you defined main bundles for the frontend, use app bundles previously defined;
* ENABLE NEEDED BUNDLE: Leading bundles you effectively want to use and expose in your templates. Bundle that are not defined here will not be reachable from templates and won't be minified;
"""
