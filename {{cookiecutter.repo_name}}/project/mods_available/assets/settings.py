# -*- coding: utf-8 -*-

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'django_assets')

# Asset debugging is linked to settings.DEBUG, when True no bundle will be compiled (use directly its source files)
ASSETS_DEBUG = DEBUG
# The asset root directory where webassets will compile bundles files
ASSETS_ROOT = join(PROJECT_PATH, 'webapp_statics/')
# Specify project's static files directory to search for assets (additionaly to apps assets)
STATICFILES_DIRS += (ASSETS_ROOT,)
# Add a manifest file, required when using placeholder in Bundle names
ASSETS_MANIFEST = "file:{0}".format(join(ASSETS_ROOT, 'webassets.manifest'))
# Add a project assets file to define project assets bundles (and not only apps assets)
ASSETS_MODULES = (
    'project.assets',
)
