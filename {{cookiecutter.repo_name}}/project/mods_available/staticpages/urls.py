# -*- coding: utf-8 -*-
from django.conf import settings
from staticpages.urls import loaders

if settings.ENABLE_STATICPAGES:
    urlpatterns = patterns('', *loaders.mount_staticpages(*settings.STATICPAGES_PROTOTYPES)) + urlpatterns
