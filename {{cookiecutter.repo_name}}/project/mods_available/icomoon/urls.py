# -*- coding: utf-8 -*-
urlpatterns = patterns('',
    url(r'^icomoon/', include('icomoon.urls', namespace='icomoon')),
    ) + urlpatterns
