"""
.. _Django Icomoon: https://github.com/sveetch/django-icomoon

`Django Icomoon`_ help you to manage your webfonts with Icomoon service. It won't work with a webfont not generated on Icomoon site because it depends on a JSON manifest file (you could make it yourself but it's a little bit complicated).

This mod can handle many webfonts if you need, you just have to define them in the mod settings, at least one webfont is required.

Once one or more webfonts are defined, `Django Icomoon`_ can help you to automatically deploy them in your project from downloaded Zip on Icomoon using a command line ``django-instance icomoon_deploy``.

Also when deployed and the webfonts are loaded in your templates, you can visualize every icons from a gallery located at ``/icomoon/``.
"""