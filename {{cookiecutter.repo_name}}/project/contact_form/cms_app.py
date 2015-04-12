"""
Apphooks for contact forms
"""
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ContactApphook(CMSApp):
    name = _("Contact form")
    urls = ["project.contact_form.urls"]


apphook_pool.register(ContactApphook)