from django.core.mail import EmailMessage

from django.conf import settings

def send_msg(file, email):
    mail = EmailMessage(
        "Hi", 
        "Success", 
        settings.EMAIL_HOST_USER, 
        [email]
    )
    # .name, file.read(), file.content_type
    mail.attach_file(file)
    mail.send()