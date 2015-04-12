# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'staticpages')

STATICPAGES_PROTOTYPES = (
    (r'prototypes/$', "prototypes/index.html", 'prototypes-index'),
    (r'prototypes/buttons/$', "prototypes/buttons.html", 'prototypes-buttons'),
    (r'prototypes/foundation5/$', "prototypes/foundation5.html", 'prototypes-foundation5'),
)
