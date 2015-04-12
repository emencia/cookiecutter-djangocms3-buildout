# -*- coding: utf-8 -*-
"""
Using crispy_forms with Foundation set
"""

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'crispy_forms', 'crispy_forms_foundation')

CRISPY_FAIL_SILENTLY = not DEBUG

# Default layout to use with "crispy_forms"
CRISPY_TEMPLATE_PACK = 'foundation-5'
