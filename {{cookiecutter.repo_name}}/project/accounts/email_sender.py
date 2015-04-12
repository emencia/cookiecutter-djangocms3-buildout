from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

def send_activation_email(user, site, user_info):

    activate_user = user.registrationprofile_set.all()[0]
    ctx_dict = {'activation_key': activate_user.activation_key,
                'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'user_info': user_info,
                'site': site}
    subject = render_to_string('registration/activation_email_subject.txt',
                               ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('registration/activation_email.txt',
                               ctx_dict)
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
              settings.DEFAULT_ACTIVE_SUBSCRIBE_EMAILS)

def send_activation_pending_email(user, site, user_info):

    ctx_dict = {'site': site,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'user_info': user_info}
    subject = render_to_string('registration/activation_pending_email_subject.txt',
                               ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('registration/activation_pending_email.txt',
                               ctx_dict)
    user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

def send_confirmation_email(user, site):

    ctx_dict = {'site': site}
    subject = render_to_string('registration/confirmation_email_subject.txt',
                               ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('registration/confirmation_email.txt',
                               ctx_dict)
    user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
