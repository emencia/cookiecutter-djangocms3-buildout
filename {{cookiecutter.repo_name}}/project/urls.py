# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


# Default base urls
urlpatterns = patterns(
    '',
    # Cause troubles with docutils usage like with codemirror
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# Mount mods 'urls.py' contents
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
mods = os.path.join(PROJECT_PATH, 'mods_enabled')
mods = [os.path.join(mods, x) for x in os.listdir(mods)]
mods.sort()
for mod in mods:
    mod = os.path.join(mod, 'urls.py')
    if os.path.isfile(mod):
        execfile(mod)


# Addditional stuff for enabled Debug mode
if settings.DEBUG:
    from django.views.generic import TemplateView

    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^500/$', TemplateView.as_view(template_name="500.html")),
        url(r'^404/$', TemplateView.as_view(template_name="404.html")),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
