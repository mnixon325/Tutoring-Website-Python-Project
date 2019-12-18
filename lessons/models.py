from django.db import models
from django.conf import settings
from django.utils import timezone


class Lesson(models.Model):
    """
    A model class representing a single lesson, which can be scheduled between one tutor and one student.
    """
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    creator = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='lesson_creators',
                                           on_delete=models.CASCADE, primary_key=False)
    tutor = models.CharField(max_length=120, blank=False)
    student = models.CharField(max_length=120, blank=False)
    completed = models.BooleanField(default=False, blank=False)
    date_time = models.DateTimeField(default=timezone.now, null=False, blank=False)
    subject = models.CharField(max_length=120, unique=False, blank=True, null=False, default="Python!")
