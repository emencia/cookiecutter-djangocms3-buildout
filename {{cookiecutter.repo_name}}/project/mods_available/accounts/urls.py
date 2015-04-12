# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^accounts/', include('project.accounts.urls')),
    ) + urlpatterns
