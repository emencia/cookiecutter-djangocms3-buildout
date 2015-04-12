# -*- coding: utf-8 -*-
"""
Various usefull tags
"""
from django import template

register = template.Library()

@register.filter(name='split', is_safe=False)
def split_string(value, arg=None):
    """
    A simple string splitter
    
    So you can do that : ::
    
        {% if LANGUAGE_CODE in "fr,en-ca,en-gb,zh-hk,it,en,de"|split:',' %}
    """
    return value.split(arg)