# -*- coding: utf-8 -*-
"""
Menu stuff for admin_tools
"""
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu

class LanguageMenuItem(items.MenuItem):
    """
    Dummy custom MenuItem to use the template with the language chooser form
    """
    title = _('Language')
    template = 'admin/admintool_language_chooser.html'
        
class CustomMenu(Menu):
    """
    Custom Menu for project admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.Bookmarks(),
            items.AppList(
                _('Applications'),
                exclude=('django.contrib.*',)
            ),
            items.AppList(
                _('Administration'),
                models=('django.contrib.*',)
            ),
        ]
        
        # Add menu entry for Filebrowser if installed
        try:
            import filebrowser
        except ImportError:
            pass
        else:
            self.children += [
                items.MenuItem(_('Filebrowser'), reverse('filebrowser:fb_browse')),
            ]
        
        # Add language switcher menu within admin
        #self.children += [
            #LanguageMenuItem(),
        #]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)
