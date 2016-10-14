# flake8: noqa
from project.settings import *

DEBUG = False

HTTPS_ENABLED = {% if cookiecutter.enable_https == 'yes' %}True{% else %}False{% endif %}

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

{% if cookiecutter.enable_https == 'yes' %}
# Since https is enabled, recaptcha have to be ssl also
RECAPTCHA_USE_SSL = True{% endif %}

{% if cookiecutter.enable_contact_form == 'yes' %}# For contact form emails
CONTACT_FORM_TO = [
    'contact@localhost',
]{% endif %}

# Email sender for various applications
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
