from django.db import models
from django.conf import settings
from rest_framework import serializers
from users.models import User


# TODO: Require sender and receiver to both be registered users.

class Message(models.Model):
    "A message between two users (sender and receiver). Either or both can be tutors or students."
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='+', null=True, blank=True)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 related_name='+', null=True, blank=True)
    subject = models.CharField(max_length=120)
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = ['-created', '-id']

    # TODO: Automatically send an email to the receiver's email address when a message is
    #  created. Use django.core.mail import send_mail :
    #  https://docs.djangoproject.com/en/2.2/topics/email/
    #  https://stackoverflow.com/questions/6367014/how-to-send-email-via-django
