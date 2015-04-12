"""
Enable `django-assets`_ to combine and minify your *assets* (CSS, JS). The minification library used, *yuicompressor*, requires the installation of Java (the OpenJDK installed by default on most Linux systems is sufficient).

In general, this component is required. If you do not intend to use it, you will need to modify the project's default templates to remove all of its occurrences.

Assets are defined in ``project/assets.py`` and some apps can defined their own ``asset.py`` file but our main file does not use them.

Our ``asset.py`` file is divised in three parts :

* BASE BUNDLES: Only for app bundle like Foundation Javascript files or RoyalSlider files;
* MAIN AVAILABLE BUNDLES: Where you defined main bundles for the frontend, use app bundles previously defined;
* ENABLE NEEDED BUNDLE: Bundle you effectively want to use. Bundle that are not defined here will not be reachable from templates and won't be compiled;
"""
