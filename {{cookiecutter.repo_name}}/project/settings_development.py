"""
Settings to use for development
"""
from settings import *

# Enable django-debug-toolbar for the following IPs
INTERNAL_IPS = ('127.0.0.1',)

# Test emails by looking at the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# googletools is disabled when settings.DEBUG is True, you can force to enable it
# with uncommenting this line
#GOOGLETOOLS_ENABLED = True

{% if cookiecutter.enable_contact_form == 'yes' %}# For contact form emails
CONTACT_FORM_TO = [
    'contact@localhost',
]{% endif %}

# Email sender for various applications
DEFAULT_FROM_EMAIL = 'webmaster@localhost'