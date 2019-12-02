from django.db import models
from users.models import User


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)
