# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^socialaggregator/', include('socialaggregator.urls')),
    ) + urlpatterns
