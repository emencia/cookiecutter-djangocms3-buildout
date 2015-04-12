# -*- coding: utf-8 -*-
"""
Forms for contact forms
"""
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.forms import ModelForm, Textarea
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from project.utils.context_processors import get_site_metas

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Field, Fieldset, Row, Column, HTML, ButtonHolder, ButtonHolderPanel, Submit, InlineField, InlineJustifiedField

from captcha.fields import ReCaptchaField

from .models import CIVILITY_CHOICES, ContactBase, Contact

def SimpleRowColumn(field, *args, **kwargs):
    """
    Shortcut for simple row with only a full column
    """
    if isinstance(field, basestring):
        field = Field(field, *args, **kwargs)
    return Row(
        Column(field),
    )

class ContactFormBase(ModelForm):
    """
    Contact base form, you cant use it directly because the used 
    model ('ContactBase') is just an abstract model
    """
    error_css_class = 'error'
    required_css_class = 'required'
    mail_subject_template = 'contact_form/contact_form_subject.txt'
    mail_content_template = 'contact_form/contact_form.txt'
   
    def __init__(self, *args, **kwargs):
        super(ContactFormBase, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_action = '.'

    def save(self, commit=True):
        """Save and send"""
        contact = super(ContactFormBase, self).save()
        context = {'contact': contact}
        context.update(get_site_metas())

        subject = ''.join(render_to_string(self.mail_subject_template, context).splitlines())
        content = render_to_string(self.mail_content_template, context)

        send_mail(subject, content,
                  settings.DEFAULT_FROM_EMAIL,
                  settings.CONTACT_FORM_TO,
                  fail_silently=not settings.DEBUG)

        return contact

    class Meta:
        model = ContactBase

class ContactForm(ContactFormBase):
    """Contact Form"""
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})
    
    def __init__(self, *args, **kwargs):
        super(ContactFormBase, self).__init__(*args, **kwargs)
        
        self.fields['civility'].choices = (('', _('civility')),) + CIVILITY_CHOICES
        
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = Contact
