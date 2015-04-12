# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'project.accounts', 'registration')

ACCOUNT_ACTIVATION_DAYS = 7
DEFAULT_FROM_EMAIL = 'noreply@dummy.com'

# Default URL to redirect to just after successful login
LOGIN_REDIRECT_URL = "/"

DEFAULT_ACTIVE_SUBSCRIBE_EMAILS = []
CONTACT_FORM_EMAILS = []
