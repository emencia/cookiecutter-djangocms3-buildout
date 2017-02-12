"""
.. _emencia-django-staticpages: https://github.com/emencia/emencia-django-staticpages

This mod uses `emencia-django-staticpages`_ to publish static pages with a
*direct to template* view.

Every ressources listed in ``settings.STATICPAGES_PROTOTYPES`` will be mounted
if ``settings.ENABLE_STATICPAGES`` is ``True``. Default behavior is to enable
these ressources on all environment excepted for production.
"""  # noqa: E501