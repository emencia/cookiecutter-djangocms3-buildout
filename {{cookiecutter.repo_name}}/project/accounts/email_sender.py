"""
Email sender methods
"""
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail


def send_activation_email(user, site, user_profile):
    """
    Send email to admin to warn them about new pending registration to activate
    """
    context = {
        'site': site,
        'activation_key': user.registrationprofile.activation_key,
        'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
        'user': user,
        'user_profile': user_profile,
    }
    subject = render_to_string('registration/activation_email_subject.txt',
                               context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    message = render_to_string('registration/activation_email.txt',
                               context)
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
              settings.DEFAULT_ACTIVE_SUBSCRIBE_EMAILS)


def send_activation_pending_email(user, site, user_profile):
    """
    Send email to notice him about pending registration
    """
    context = {
        'site': site,
        'user': user,
        'user_profile': user_profile,
    }
    subject = render_to_string('registration/activation_pending_email_subject.txt',
                               context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('registration/activation_pending_email.txt',
                               context)
    user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)


def send_confirmation_email(user, site):
    """
    Send email to user to confirm is registration
    """
    context = {
        'site': site,
    }
    subject = render_to_string('registration/confirmation_email_subject.txt',
                               context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('registration/confirmation_email.txt',
                               context)
    user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
