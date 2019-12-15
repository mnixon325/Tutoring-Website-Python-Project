from django.db import models
from users.models import User


# TODO: Require sender and receiver to both be registered users.

class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # sender = models.CharField(null=False, max_length=50)
    # receiver = models.CharField(null=False, max_length=50)
    sender = models.ForeignKey('users.User', related_name="sender", on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey('users.User', related_name="receiver", on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)

    # TODO: Automatically send an email to the receiver's email address when a message is
    #  created. Use django.core.mail import send_mail :
    #  https://docs.djangoproject.com/en/2.2/topics/email/
    #  https://stackoverflow.com/questions/6367014/how-to-send-email-via-django
