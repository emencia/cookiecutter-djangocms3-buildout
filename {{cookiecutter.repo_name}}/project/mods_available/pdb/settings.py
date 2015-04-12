# -*- coding: utf-8 -*-
MIDDLEWARE_CLASSES += (
    'django_pdb.middleware.PdbMiddleware',
)

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'django_pdb')
