# -*- coding: utf-8 -*-

# Import from the Standard Library
import os

# Import from django
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')), # Cause troubles with docutils usage like with codemirror
    url(r'^admin/', include(admin.site.urls)),
)

# Mods system
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
mods = os.path.join(PROJECT_PATH, 'mods_enabled')
mods = [ os.path.join(mods, x) for x in os.listdir(mods) ]
mods.sort()
for mod in mods:
    mod = os.path.join(mod, 'urls.py')
    if os.path.isfile(mod):
        execfile(mod)

# Debug
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^500/$', TemplateView.as_view(template_name="500.html")),
        url(r'^404/$', TemplateView.as_view(template_name="404.html")),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
