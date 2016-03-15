# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'django_comments',
    'tagging',
    'zinnia',
    'cmsplugin_zinnia',
    'zinnia_ckeditor',
)

TEMPLATES[0]['OPTIONS']['context_processors'] = add_to_tuple(
    TEMPLATES[0]['OPTIONS']['context_processors'],
    'zinnia.context_processors.version',
)

# List entries by ..
ZINNIA_PAGINATION = 3

## Comments disabled by default
#ZINNA_AUTO_CLOSE_COMMENTS_AFTER = 0

# Optional additional zinnia cms plugin templates
CMSPLUGIN_ZINNIA_TEMPLATES = [
    #('cmsplugin_zinnia/homepage_entry_list.html', 'home'),
]