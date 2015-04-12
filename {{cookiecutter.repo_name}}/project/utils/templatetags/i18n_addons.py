# -*- coding: utf-8 -*-
"""
Common templates tags for porticus
"""
#from django.conf import settings
from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from django.conf import settings

from porticus.models import Gallery, Album

gettext = lambda s: s

register = template.Library()

def locale_title(locale_name):
    """
    Giving a locale name return its title, taken from the settings.EXTRA_COUNTRY_LOCALES
    
    If the locale is not in the settings.EXTRA_COUNTRY_LOCALES, return it unchanged
    """
    l = dict(settings.EXTRA_COUNTRY_LOCALES)
    if locale_name not in l:
        return locale_name
    return l.get(locale_name)

register.simple_tag(locale_title)
register.filter('locale_title', locale_title)

def is_valid_locale_name(locale_name):
    """
    Giving a locale name return a boolean wether the locale is in settings.EXTRA_COUNTRY_LOCALES or not
    """
    return (locale_name in dict(settings.EXTRA_COUNTRY_LOCALES))

register.assignment_tag(is_valid_locale_name)
