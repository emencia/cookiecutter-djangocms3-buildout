"""
Settings for django-recaptcha module
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'captcha')

# You MUST edit the following keys with your reCaptcha account keys
RECAPTCHA_PUBLIC_KEY = 'dummy-public'
RECAPTCHA_PRIVATE_KEY = 'dummy-private'
