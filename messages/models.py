from django.db import models


class Message(models.Model):
    "A message between two users (sender and receiver). Either or both can be tutors or students."
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sender = models.CharField(max_length=120)
    receiver = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    content = models.TextField(blank=True, max_length=1000)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = ['-created', '-id']
