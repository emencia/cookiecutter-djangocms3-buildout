"""
.. 

Enable `django-sendfile`_ that is somewhat like a helper around the **X-SENDFILE headers**, a technic to process some requests before let them pass to the webserver.

Commonly used to check for permissions rights to download some private files before let the webserver to process the request. So the webapp can execute some code on a request without to carry the file to download (than could be a big issue with some very big files).

`django-sendfile`_ dependancy in the buildout config is commented by default, so first you will need to uncomment its line to install it, before enabling the mod. Then you will need to create the directory to store the protected medias, because if you store them in the common media directory, they will public to everyone.

This directory must be in the project directory, then its name can defined in the ``PROTECTED_MEDIAS_DIRNAME`` mod setting, default is to use ``protected_medias`` and so you should create the ``project/protected_medias`` directory.

**Your webserver need to support this technic**, no matter on a recent nginx as it is allready embeded in, on Apache you will need to install the Apache module XSendfile (it should be availabe on your distribution packages) and enable it in the virtualhost config (or the global one if you want), see the `Apache module documentation <https://tn123.org/mod_xsendfile/>`_ for more details. Then remember to update your virtualhost config with the needed directive, use the Apache config file builded from buildout.

The nginx config template allready embed a rule to manage ``project/protected_medias`` with sendfile, but it is commented by default, so you will need to uncomment it before to launch buildout again to build the nginx config file.

.. note::
        By default, the mod use the django-sendfile's backend for development that is named ``sendfile.backends.development``. For production, you will need to use the right backend for your webserver (like ``sendfile.backends.nginx``).

Finally you will need to implement it in your code as this will require a custom view to download the file, see the `django-sendfile`_  documentation for details about this. But this is almost easy, you just need to use the ``sendfile.sendfile`` method to return the right Response within your view.
"""