# -*- coding: utf-8 -*-
urlpatterns = patterns('',
    url(r'^galleries/', include('porticus.urls', namespace='porticus')),
    ) + urlpatterns
