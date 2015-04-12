INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 
    'admin_shortcuts',
    'djangocms_admin_style',
    before="django.contrib.admin"
)

ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
            },
            {
                'url_name': 'admin:cms_page_changelist',
                'title': gettext('Pages'),
            },
            {
                'url_name': 'filebrowser:fb_browse',
                'title': gettext('Files'),
            },
            {
                'url_name': 'admin:auth_user_changelist',
                'title': gettext('Users'),
            },
        ]
    },
]