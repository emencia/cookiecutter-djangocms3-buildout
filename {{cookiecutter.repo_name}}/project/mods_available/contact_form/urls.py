# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^contact/', include('project.contact_form.urls')),
    ) + urlpatterns
