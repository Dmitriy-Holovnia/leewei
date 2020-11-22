from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


UserModel = get_user_model()

def send_confirmation_email(request, user, email):
    site = get_current_site(request)
    mail_subject = 'Leewei Trading :: Activate your account'
    message = render_to_string('mail/activate-mail.html', {
      'user': user,
      'domain': site.domain,
      'uid': urlsafe_base64_encode(force_bytes(user.pk)),
      'token': default_token_generator.make_token(user),
    })
    mail = EmailMessage(mail_subject, message, to=[email])
    mail.send()

def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True
    else:
        return False

