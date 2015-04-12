# -*- coding: utf-8 -*-
"""
Models for contact forms
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from emencia.django.countries.models import Country

CIVILITY_CHOICES = (
    (0, _('mlle')),
    (1, _('mme')),
    (2, _('mr')),
)

class ContactBase(models.Model):
    """Models for storing contact message"""
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)

    civility = models.IntegerField(_('civility'), choices=CIVILITY_CHOICES)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField(_('email'))
    message = models.TextField(_('message'), blank=True)

    def __unicode__(self):
        return 'Contact from %s %s' % (self.first_name, self.last_name)

    class Meta:
        abstract = True
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

class Contact(ContactBase):
    """Default enabled model"""
    phone = models.CharField(_('phone'), max_length=15)
    company = models.CharField(_('company'), max_length=250, blank=True)
    city = models.CharField(_('city'), max_length=255, blank=True)
    state = models.CharField(_('state/province'), max_length=255, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('country'), blank=True, null=True)
    optin_newsletter = models.BooleanField(_("do you wish to receive the newsletter?"), default=False)
