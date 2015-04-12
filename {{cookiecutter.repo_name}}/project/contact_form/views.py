# -*- coding: utf-8 -*-
"""
Views for contact forms
"""
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView

from .forms import ContactForm

class ContactFormBaseView(FormView):
    """
    Base view for contact forms
    """
    template_name = 'contact_form/contact_form.html'
    form_class = ContactForm
    
    def get_success_url(self):
        return reverse('contact_form_sent')

    def form_valid(self, form):
        form.save()
        return super(ContactFormBaseView, self).form_valid(form)


class ContactFormView(ContactFormBaseView):
    """Contact form view"""
    form_class = ContactForm
