# -*- coding: utf-8 -*-
"""
Urls for contact forms
"""
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from .views import ContactFormView

urlpatterns = patterns('project.contact_form.views',
    url(r'^$', ContactFormView.as_view(), name='contact_form')
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^sent/$', TemplateView.as_view(template_name='contact_form/contact_form_sent.html'), name='contact_form_sent')
)
