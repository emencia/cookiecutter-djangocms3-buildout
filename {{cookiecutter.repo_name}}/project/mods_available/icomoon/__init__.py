"""
.. _Django Icomoon: https://github.com/sveetch/django-icomoon

`Django Icomoon`_ display a gallery of all your defined Icomoon webfonts. It won't work with a webfont not generated on Icomoon site because it depends on a JSON manifest file.

Default behavior is to search for the JSON manifest file at ``project/webapp_statics/fonts/selection.json``, so when you deploy an icomoon webfont you have to put there the ``selection.json`` file given into the download ZIP archive.

If you have more than one Icomoon webfont in your project, you can define more manifest to search for, read the documentation for more details.

Once the JSON manifest installed, along the webfont files, you can reach the gallery at : ::

    /icomoon/

Default behavior is to required to be authenticated to access to the gallery.
"""