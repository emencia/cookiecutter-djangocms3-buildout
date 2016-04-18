# -*- coding: utf-8 -*-
"""
Settings to enable admin_tools
"""
ADMIN_TOOLS_MENU = "project.mods_enabled.admin_tools.menu.CustomMenu"
ADMIN_TOOLS_INDEX_DASHBOARD = "project.mods_enabled.admin_tools.dashboard.CustomIndexDashboard"
ADMIN_TOOLS_APP_INDEX_DASHBOARD = "project.mods_enabled.admin_tools.dashboard.CustomAppIndexDashboard"

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    before='django.contrib.admin')

TEMPLATES[0]['OPTIONS']['context_processors'] = add_to_tuple(
    TEMPLATES[0]['OPTIONS']['context_processors'],
    'django.core.context_processors.request',
)
