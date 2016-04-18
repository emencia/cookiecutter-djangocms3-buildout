# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'autobreadcrumbs')

# Global map where you can define every breadcrumbs that don't resides in
# their application
AUTOBREADCRUMBS_TITLES = {
    'pages-root': 'Accueil',
}

TEMPLATES[0]['OPTIONS']['context_processors'] = add_to_tuple(
    TEMPLATES[0]['OPTIONS']['context_processors'],
    'autobreadcrumbs.context_processors.AutoBreadcrumbsContext'
)
