from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserInfo(models.Model):
    """
    To deprecate, this is not accurate with "Custom model user" capacities 
    since django 1.5, better should implement it instead
    """
    user = models.ForeignKey(User, unique=True, verbose_name=_('user'))

    company = models.CharField(_('Company'), max_length=100)
    function = models.CharField(_('Function'), max_length=256)
    address = models.TextField(_('Address'), blank=True)
    postal_code = models.CharField(_('Postal code'), max_length=15, blank=True)
    city = models.CharField(_('City'), max_length=100, blank=True)
    country = models.CharField(_('Country'), max_length=100, blank=True)
    phone = models.CharField(_('Professional phone number'), max_length=25, blank=True)
