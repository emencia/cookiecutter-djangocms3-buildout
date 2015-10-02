# -*- coding: utf-8 -*-
"""
Using crispy_forms with Foundation set
"""

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'crispy_forms', 'crispy_forms_foundation')

CRISPY_FAIL_SILENTLY = not DEBUG

# Add 'foundation-5' layout pack
CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap', 'uni_form', 'bootstrap3', 'foundation-5')

# Default layout to use with "crispy_forms"
CRISPY_TEMPLATE_PACK = 'foundation-5'
