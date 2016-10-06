# -*- coding: utf-8 -*-
from icomoon.settings import *

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'icomoon')

ICOMOON_WEBFONTS = {
    'Default': {
        'fontdir_path': join(PROJECT_PATH, 'webapp_statics/fonts'),
        'csspart_path': join(PROJECT_PATH, '..', "sass/scss/components/_icomoon_icons.scss"),
    },
}
