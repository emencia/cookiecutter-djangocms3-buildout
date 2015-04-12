# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'django_comments',
    'tagging',
    'zinnia',
    'cmsplugin_zinnia',
    'zinnia_ckeditor',
)

# List entries by ..
ZINNIA_PAGINATION = 3

TEMPLATE_CONTEXT_PROCESSORS += (
    'zinnia.context_processors.version',
)
