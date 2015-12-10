"""
Admins for contact forms
"""
from django.contrib import admin
from django.utils.translation import ugettext as _

# use django-import-export to export contact list
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Import from here
from models import Contact

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class ContactBaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    list_display = ('last_name', 'first_name', 'email', 'creation_date')
    list_filter = ('creation_date',)
    search_fields = ('first_name', 'last_name', 'email', 'message')
    fieldsets = ((None, {'fields': ('civility', 'first_name', 'last_name',
                                    'email',)}),
                 (None, {'fields': ('message',)}),
        )
    actions_on_top = False
    actions_on_bottom = True


class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource
    list_display = ('last_name', 'first_name', 'company', 'email', 'phone',
                    'city', 'country', 'optin_newsletter', 'creation_date')

    list_filter = ('creation_date', 'optin_newsletter')
    search_fields = ('first_name', 'last_name', 'company', 'email', 'phone',
                     'city', 'state')
    fieldsets = ((None, {'fields': ('civility', 'first_name', 'last_name',
                                    'company')}),
                 (None, {'fields': ('message',)}),
                 (_('Contact'), {'fields': ('email', 'phone',
                                 'optin_newsletter')}),
                 (_('Address'), {'fields': ('city', 'state', 'country')}),)

admin.site.register(Contact, ContactAdmin)
