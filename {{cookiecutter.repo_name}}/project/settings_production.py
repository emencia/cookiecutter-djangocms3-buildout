from project.settings import *

DEBUG = False

ASSETS_DEBUG = False
ASSETS_ROOT = STATIC_ROOT
ASSETS_AUTO_BUILD = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',               # Set to empty string for default.
    }
}

RAVEN_CONFIG = {
    'dsn': '',
}

INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
