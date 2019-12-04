from django.db import models
from users.models import User


# TODO: Require sender and receiver to both be registered users.

class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sender = models.CharField(null=False, max_length=50)
    receiver = models.CharField(null=False, max_length=50)
    # sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE, null=True)
    # receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)
