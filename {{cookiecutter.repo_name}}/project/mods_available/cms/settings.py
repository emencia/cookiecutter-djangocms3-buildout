# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'cms',  # Django CMS core
    'treebeard',  # utilities for implementing a modified pre-order traversal tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'djangocms_snippet',
    #'reversion', # not really needed for now
)

MIDDLEWARE_CLASSES += (
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
{% if cookiecutter.enable_multiple_languages == 'yes' %}
    'cms.middleware.language.LanguageCookieMiddleware',{% endif %}
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
