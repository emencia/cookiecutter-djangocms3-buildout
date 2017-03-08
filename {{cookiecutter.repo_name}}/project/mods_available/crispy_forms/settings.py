# -*- coding: utf-8 -*-
"""
Using crispy_forms with Foundation set
"""

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'crispy_forms', 'crispy_forms_foundation')

from crispy_forms_foundation.settings import *

CRISPY_FAIL_SILENTLY = not DEBUG
