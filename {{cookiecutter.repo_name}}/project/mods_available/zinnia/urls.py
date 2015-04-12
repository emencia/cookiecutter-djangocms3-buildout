# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^news/', include('zinnia.urls', namespace='zinnia')),
    # Comments are disabled by default
    #url(r'^comments/', include('django_comments.urls')),
    ) + urlpatterns
