from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from django.contrib.auth.views import login as login_base
from django.contrib.auth.views import password_change as password_change_base
from django.contrib.auth.views import password_reset as password_reset_base
from django.contrib.auth.views import password_reset_confirm as password_reset_confirm_base

from registration.backends.default.views import RegistrationView as RegisView
from registration.backends.default.views import ActivationView as ActView
from registration.models import RegistrationProfile
from registration import signals

from .models import UserInfo
from .forms import AuthenticationFormAccounts, PasswordChangeFormAccounts, PasswordResetFormAccounts, SetPasswordFormAccounts, RegistrationFormAccounts

from .email_sender import send_activation_email, send_activation_pending_email, send_confirmation_email

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
    Overload on Registration class
    """
    form_class = RegistrationFormAccounts

    def register(self, request, **cleaned_data):
        """
        Given a username, email address and password, register a new
        user account, which will initially be inactive.

        Along with the new ``User`` object, a new
        ``registration.models.RegistrationProfile`` will be created,
        tied to that ``User``, containing the activation key which
        will be used for this account.

        Two emails will be sent. First one to the admin; this email should
        contain an activation link and a resume of the new user infos.
        Second one, to the user, for inform him that his request is pending.

        After the ``User`` and ``RegistrationProfile`` are created and
        the activation email is sent, the signal
        ``registration.signals.user_registered`` will be sent, with
        the new ``User`` as the keyword argument ``user`` and the
        class of this backend as the sender.

        """
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
            
        create_user = RegistrationProfile.objects.create_inactive_user
        new_user = create_user(
            cleaned_data['username'],
            cleaned_data['email'],
            cleaned_data['password1'],
            site,
            send_email=False
        )
        new_user.first_name = cleaned_data['first_name']
        new_user.last_name = cleaned_data['last_name']
        new_user.save()
        
        user_info = UserInfo(
            user=new_user,
            company=cleaned_data['company'],
            function=cleaned_data['function'],
            address=cleaned_data['address'],
            postal_code=cleaned_data['postal_code'],
            city=cleaned_data['city'],
            country=cleaned_data['country'],
            phone=cleaned_data['phone'],
        )
        user_info.save()
        
        send_activation_email(new_user, site, user_info)
        send_activation_pending_email(new_user, site, user_info)
        
        signals.user_registered.send(sender=self.__class__, user=new_user, request=request)
        
        return new_user


class ActivationView(ActView):
    def activate(self, request, activation_key):
        user = super(ActivationView, self).activate(request, activation_key)
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        if user:
            send_confirmation_email(user, site)
        return user
