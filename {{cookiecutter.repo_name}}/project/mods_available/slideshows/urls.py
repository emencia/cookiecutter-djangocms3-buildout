# -*- coding: utf-8 -*-
urlpatterns = patterns('',
    url(r'^slideshows/', include('slideshows.urls', namespace='slideshows')),
    ) + urlpatterns
