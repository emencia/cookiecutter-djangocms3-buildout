# -*- coding: utf-8 -*-
# flake8: noqa

urlpatterns = patterns(
    '',
    url(r'^admin/datadownloader', include('datadownloader.urls')),
    ) + urlpatterns
