"""
Settings to enable the django-debug-toolbar
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'debug_toolbar', before="cms")

# Must match the IP adress you will use to access to the instance
INTERNAL_IPS = ()

DEBUG_TOOLBAR_PATCH_SETTINGS = True

# Options 
DEBUG_TOOLBAR_PANELS = [
    #'debug_toolbar.panels.versions.VersionsPanel',
    #'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    #'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    #'debug_toolbar.panels.cache.CachePanel',
    #'debug_toolbar.panels.signals.SignalsPanel',
    #'debug_toolbar.panels.logging.LoggingPanel',
    #'debug_toolbar.panels.redirects.RedirectsPanel',
]


# Registering the debug_toolbar app and middleware
MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) \
                     + MIDDLEWARE_CLASSES
