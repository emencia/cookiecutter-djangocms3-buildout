# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    ) + urlpatterns
