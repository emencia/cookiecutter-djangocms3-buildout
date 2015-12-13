"""
.. _Django reCaptcha: https://github.com/praekelt/django-recaptcha
.. _Django registration: https://github.com/macropin/django-registration

Enable `Django registration`_ and everything you need to allow users to register and to connect/disconnect. Sample views and forms are include so it can be easily used. 

It includes:

* A view for the login and one for the logout;
* All the views for the registration request (request, confirmation, etc.);
* A view to ask for the reinitialization of a password;
* Email sending;

In the ``skeleton.html`` template, a partial HTML code is commented. Uncomment it to display the *logout* button when the user is connected.

The registration process consists in sending an email (sender/destination emails have to be configured in settings) with the registration request to an administrator responsible for accepting them (or not). Once validated, an email is sent to the user to confirm his registration by way of a link. Once this step has been completed, the user can connect.

Also, note that this app extend the user model with a profile model. 

This profile is naive because it implement some comon additional fields for sample but you may not need all of them, if you change it you will need to do some changes also in registration view, forms and email senders.

.. note::
   Included forms and templates depends on `crispy_forms`_ mod.
"""