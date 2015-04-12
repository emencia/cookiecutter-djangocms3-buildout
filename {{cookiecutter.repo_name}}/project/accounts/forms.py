from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, Row, Column, ButtonHolder, Submit

from registration.forms import RegistrationFormUniqueEmail

def dummy_form_helper():
    """
    Return a very simple form helper that will only display the input fields from the 
    form and the csrf.
    
    <form/> tag and submit button is at your charge in the templates, fields are 
    automatically selected from the form and csrf is inserted.
    """
    helper = FormHelper()
    helper.form_tag = False
    
    return helper

class AuthenticationFormAccounts(AuthenticationForm):
    """
    Override the default form to add a very simple crispy_forms helper
    """
    def __init__(self, *args, **kwargs):
        self.helper = dummy_form_helper()
        
        super(AuthenticationFormAccounts, self).__init__(*args, **kwargs)

class PasswordChangeFormAccounts(PasswordChangeForm):
    """
    Override the default form to add a very simple crispy_forms helper
    """
    def __init__(self, *args, **kwargs):
        self.helper = dummy_form_helper()
        
        super(PasswordChangeFormAccounts, self).__init__(*args, **kwargs)

class PasswordResetFormAccounts(PasswordResetForm):
    """
    Override the default form to add a very simple crispy_forms helper
    """
    def __init__(self, *args, **kwargs):
        self.helper = dummy_form_helper()
        
        super(PasswordResetFormAccounts, self).__init__(*args, **kwargs)

class SetPasswordFormAccounts(SetPasswordForm):
    """
    Override the default form to add a very simple crispy_forms helper
    """
    def __init__(self, *args, **kwargs):
        self.helper = dummy_form_helper()
        
        super(SetPasswordFormAccounts, self).__init__(*args, **kwargs)



class RegistrationFormAccounts(RegistrationFormUniqueEmail):
    """
    Form for registration
    """
    first_name = forms.CharField(label=_('Firstname'), required=False)
    last_name = forms.CharField(label=_('Lastname'))
    company = forms.CharField(label=_('Company'))
    function = forms.CharField(label=_('Function'))
    address = forms.CharField(label=_('Address'), required=False, widget=forms.Textarea(attrs={'rows':3}))
    postal_code = forms.CharField(label=_('Postal code'), required=False)
    city = forms.CharField(label=_('City'), required=False)
    country = forms.CharField(label=_('Country'), required=False)
    phone = forms.CharField(label=_('Professional phone number'), required=False)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Fieldset(
                _('User'),
                Row(
                    Column(
                        'username',
                        css_class='six'
                    ),
                    Column(
                        Row(
                            Column(
                                'password1',
                                css_class='six unpadded'
                            ),
                            Column(
                                'password2',
                                css_class='six unpadded'
                            ),
                        ),
                        css_class='six'
                    ),
                ),
            ),
            Fieldset(
                _('Society'),
                Row(
                    Column(
                        'company',
                        css_class='six'
                    ),
                    Column(
                        'function',
                        css_class='six'
                    ),
                ),
            ),
            Fieldset(
                _('Personal details'),
                Row(
                    Column(
                        Row(
                            Column(
                                'first_name',
                                css_class='six unpadded'
                            ),
                            Column(
                                'last_name',
                                css_class='six unpadded'
                            ),
                        ),
                        css_class='six'
                    ),
                    Column(
                        'email',
                        css_class='six'
                    ),
                ),
                Row(
                    Column(
                        'address',
                        css_class='six'
                    ),
                    Column(
                        Row(
                            Column(
                                'city',
                                css_class='eight unpadded'
                            ),
                            Column(
                                'postal_code',
                                css_class='four unpadded'
                            ),
                            Column(
                                'country',
                                css_class='six unpadded'
                            ),
                            Column(
                                'phone',
                                css_class='six unpadded'
                            ),
                        ),
                        css_class='six'
                    ),
                ),
            ),
            Row(
                Column(
                    ButtonHolder( Submit('submit', _('Submit')), css_class="text-right" ),
                    css_class='twelve'
                ),
            )
        )
        
        super(RegistrationFormAccounts, self).__init__(*args, **kwargs)
