"""
.. _django-assets: https://github.com/miracle2k/django-assets/
.. _rcssmin: https://github.com/ndparker/rcssmin
.. _googleclosure: https://developers.google.com/closure/compiler/

Enable `django-assets`_ to combine and minify your *assets* (CSS, JS).

There are two used minification libraries:

* `rcssmin`_ for CSS;
* `googleclosure`_ for Javascript;

``googleclosure`` requires a Java install (OpenJDK installed on most Linux systems is sufficient), it is installed through a Python meta package including a Jar file.

Generally, this mod is required. If you do not intend to use it, you will need to modify the project's default templates to remove all of its occurrences.

Assets are defined in ``project/assets.py`` and some apps can defined their own ``assets.py`` file but our main file does not use them.
"""
