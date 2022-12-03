from django.conf import settings
from django.core.mail import send_mail


def send_acc_activation(email,email_token):
    subject="your account needs to be verified"
    email_from=settings.EMAIL_HOST_USER
    message=f"yo , click on the link to activate your account http://127.0.0.1:8000/activate/{email_token}"
    send_mail(subject,message,email_from,[email])
