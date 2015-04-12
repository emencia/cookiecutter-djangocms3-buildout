# -*- coding: utf-8 -*-
"""
Include the urls map from django-cms
"""
# Common cms url map for one language only
#urlpatterns += patterns('', url(r'^', include('cms.urls')))

# Remove the previous code line and uncomment the followings to support multiple languages
from django.conf.urls.i18n import i18n_patterns

urlpatterns += i18n_patterns('', url(r'^', include('cms.urls')))
