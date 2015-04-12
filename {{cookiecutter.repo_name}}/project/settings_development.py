"""
Settings to use for development
"""
from settings import *

# Enable django-debug-toolbar for the following IPs
INTERNAL_IPS = ('127.0.0.1',)

# Test emails by looking at the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# googletools is disabled when DEBUG=True, you can force to enable it with 
# uncommenting this line
#GOOGLETOOLS_ENABLED = True
