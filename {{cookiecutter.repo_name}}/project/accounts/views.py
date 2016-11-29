from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from django.contrib.auth.views import login as login_base
from django.contrib.auth.views import password_change as password_change_base
from django.contrib.auth.views import password_reset as password_reset_base
from django.contrib.auth.views import password_reset_confirm as \
    password_reset_confirm_base

from registration.backends.default.views import RegistrationView as RegisView
from registration.backends.default.views import ActivationView as ActView

from .models import UserProfile
from .forms import AuthenticationFormAccounts, PasswordChangeFormAccounts
from .forms import PasswordResetFormAccounts, SetPasswordFormAccounts
from .forms import RegistrationFormAccounts

from .email_sender import send_activation_email, send_activation_pending_email
from .email_sender import send_confirmation_email


def login(*args, **kwargs):
    """
    Override view to use a custom Form
    """
    kwargs['authentication_form'] = AuthenticationFormAccounts
    return login_base(*args, **kwargs)


def password_change(*args, **kwargs):
    """
    Override view to use a custom Form
    """
    kwargs['password_change_form'] = PasswordChangeFormAccounts
    return password_change_base(*args, **kwargs)


def password_reset(*args, **kwargs):
    """
    Override view to use a custom Form
    """
    kwargs['password_reset_form'] = PasswordResetFormAccounts
    return password_reset_base(*args, **kwargs)


def password_reset_confirm(*args, **kwargs):
    """
    Override view to use a custom Form
    """
    kwargs['set_password_form'] = SetPasswordFormAccounts
    return password_reset_confirm_base(*args, **kwargs)


class RegistrationView(RegisView):
    """
    Overload Registration class to fill additional user profile datas and
    send activation email to admins
    """
    form_class = RegistrationFormAccounts
    SEND_ACTIVATION_EMAIL = False

    def register(self, request, form):
        # Note than the 'register' ancestor method will send 'user_registered'
        # signal, but at this point all datas are not filled yet. So you
        # better not rely on this signal.
        new_user = super(RegistrationView, self).register(request, form)

        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        # Damned 'register' ancestor does not save first and last name..
        new_user.first_name = form.cleaned_data['first_name']
        new_user.last_name = form.cleaned_data['last_name']
        new_user.save()

        # Fill profile
        user_profile = UserProfile(
            user=new_user,
            company=form.cleaned_data['company'],
            function=form.cleaned_data['function'],
            address=form.cleaned_data['address'],
            postal_code=form.cleaned_data['postal_code'],
            city=form.cleaned_data['city'],
            country=form.cleaned_data['country'],
            phone=form.cleaned_data['phone'],
        )
        user_profile.save()

        # Send emails to user and admin(s)
        send_activation_email(new_user, site, user_profile)
        send_activation_pending_email(new_user, site, user_profile)

        return new_user


class ActivationView(ActView):
    """
    Overload Activation view to send confirmation email when succeeded
    """
    def activate(self, request, activation_key):
        user = super(ActivationView, self).activate(request, activation_key)

        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        if user:
            send_confirmation_email(user, site)
        return user
