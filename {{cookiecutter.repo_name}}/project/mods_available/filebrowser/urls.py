# -*- coding: utf-8 -*-
from filebrowser.sites import site as filebrowser_site

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(filebrowser_site.urls)),
    ) + urlpatterns
