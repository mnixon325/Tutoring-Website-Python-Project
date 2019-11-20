from django.db import models


class Lesson(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    owner = models.ForeignKey('users.User', related_name='lessons', on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    img = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
