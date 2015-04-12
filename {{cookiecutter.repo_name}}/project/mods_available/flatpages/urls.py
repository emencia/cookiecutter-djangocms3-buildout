# -*- coding: utf-8 -*-
"""
Map your flatpages urls
"""
# You can map them on a single entry point
#urlpatterns = patterns('',
    #('^pages/', include('django.contrib.flatpages.urls')),
#) + urlpatterns

# OR you can hardcode your flatpages here, this is more easy to avoid clash within a big 
# project with only some flatpages
#urlpatterns = patterns('django.contrib.flatpages.views',
    #url(r'^your-page/$', 'flatpage', {'url': '/your-page/'}, name='your-page'),
#) + urlpatterns