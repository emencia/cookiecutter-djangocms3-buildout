# -*- coding: utf-8 -*-
"""
Include the urls map from django-cms
"""
# Common CMS url map for an unique language site
{% if cookiecutter.enable_multiple_languages == 'yes' %}#{% endif %}urlpatterns += patterns('', url(r'^', include('cms.urls')))

# CMS url map to support multiple languages
{% if cookiecutter.enable_multiple_languages != 'yes' %}#{% endif %}from django.conf.urls.i18n import i18n_patterns
{% if cookiecutter.enable_multiple_languages != 'yes' %}#{% endif %}urlpatterns += i18n_patterns('', url(r'^', include('cms.urls')))
