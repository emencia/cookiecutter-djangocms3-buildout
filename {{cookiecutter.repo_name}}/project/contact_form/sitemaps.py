# -*- coding: utf-8 -*-
"""
Base sitemap entries for available forms
"""
import os, datetime

from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from project.contact_form import forms

class ContactFormEntryBase(object):
    """
    Dummy object to simulate a model entry because contact forms did not have a model
    
    So this will a inherit of ``ContactFormEntryBase`` you will have to use in 
    ``ContactFormSitemapBase.contact_forms`` to exposes your contact forms in the sitemap.
    """
    url_name = None # You contact form MUST have an url name
    priority = None # Optional custom priority
    
    def get_pub_date(self):
        """
        Implement this method if you want to return a custom last modification datetime
        """
        return None

class ContactFormSitemapBase(Sitemap):
    """
    Simple sitemap for contact forms, because they are not database entries, only just forms
    """
    changefreq = "never"
    priority_base = 1.0
    contact_forms = []
    # We determine the default last modification datetime from the forms file 
    # modification time because we don't have any other date to check for forms
    global_pub_date = datetime.datetime.fromtimestamp(os.path.getmtime(forms.__file__))

    def items(self):
        return [item() for item in self.contact_forms]
    
    def location(self, obj):
        return reverse(obj.url_name)
    
    def priority(self, obj):
        return obj.priority or self.priority_base
    
    def lastmod(self, obj):
        return obj.get_pub_date() or self.global_pub_date
    