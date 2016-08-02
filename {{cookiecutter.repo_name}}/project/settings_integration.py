from project.settings import *

DEBUG = False

ASSETS_DEBUG = False
ASSETS_ROOT = STATIC_ROOT
ASSETS_AUTO_BUILD = False

HTTPS_ENABLED = {% if cookiecutter.enable_https == 'yes' %}True{% else %}False{% endif %}

{% if cookiecutter.enable_https == 'yes' %}# Since https is enabled, recaptcha have to be ssl also
RECAPTCHA_USE_SSL = True{% endif %}

{% if cookiecutter.enable_contact_form == 'yes' %}# For contact form emails
CONTACT_FORM_TO = [
    'contact@localhost',
]{% endif %}

# Email sender for various applications
DEFAULT_FROM_EMAIL = 'webmaster@localhost'