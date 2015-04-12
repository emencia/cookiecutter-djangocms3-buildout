# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a modified pre-order traversal tree
    'menus',  # helper for model independent hierarchical website navigation
    'south',  # intelligent schema and data migrations
    'sekizai',  # for javascript and css management
    'djangocms_snippet',
    #'reversion', # raise error on south migration, there is a bug with the last version and django1.6
)

MIDDLEWARE_CLASSES = add_to_tuple(MIDDLEWARE_CLASSES,
    'django.middleware.locale.LocaleMiddleware',
    before='django.middleware.common.CommonMiddleware')


MIDDLEWARE_CLASSES += (
    'django.middleware.doc.XViewMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = add_to_tuple(TEMPLATE_CONTEXT_PROCESSORS,
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

CMS_TEMPLATES = (
    ('pages/1_cols.html', '1 column'),
    ('pages/2_cols.html', '2 columns'),
    ('pages/2_cols.autonav.html', '2 columns (1col with auto-nav)'),
    ('pages/3_cols.html', '3 columns'),
)

# Uncomment this to enable per-object user permission
# See http://docs.django-cms.org/en/latest/advanced/permissions_reference.html
#CMS_PERMISSION = True
