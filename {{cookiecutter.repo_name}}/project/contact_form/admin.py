"""
Admins for contact forms
"""
from datetime import datetime
from django.contrib import admin
from django.conf.urls import patterns, url
from django.utils.translation import ugettext as _

# Import from django-excel-response
from excel_response import ExcelResponse

# Import from here
from models import ContactBase, Contact


class ContactBaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    list_display = ('first_name', 'last_name', 'email', 'phone', 'creation_date')
    list_filter = ('creation_date',)
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'message')
    fieldsets = ((None, {'fields': ('civility', 'first_name', 'last_name',
                                    'email', 'phone', 'company')}),
                 (None, {'fields': ('message',)}),
        )
    actions_on_top = False
    actions_on_bottom = True

    def export(self, request):
        return ExcelResponse(
            ContactBase.objects.all(),
            'contact_form_%s' % datetime.now().strftime('%Y%m%d%H%M'))

    def get_urls(self):
        urls = super(ContactBaseAdmin, self).get_urls()
        my_urls = patterns(
            '',
            url(r'^export/$', self.admin_site.admin_view(self.export))
            )
        return my_urls + urls

class ContactAdmin(ContactBaseAdmin):
    list_display = ('first_name', 'last_name', 'company', 'city', 'country', 'creation_date')

    search_fields = ('first_name', 'last_name', 'company', 'email', 'phone', 'city', 'state')
    fieldsets = ((None, {'fields': ('first_name', 'last_name',
                                    'company')}),
                 (None, {'fields': ('message',)}),
                 (_('Contact'), {'fields': ('email', 'phone')}),
                 (_('Address'), {'fields': ('city', 'state', 'country')}),)

admin.site.register(Contact, ContactAdmin)
