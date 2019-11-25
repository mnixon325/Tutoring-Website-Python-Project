from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    img_profile = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    qualifications = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    travelPolicy = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    hourlyRate = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    is_student = models.BooleanField('student status', default=False)
    is_tutor = models.BooleanField('tutor status', default=False)


# TODO: Should Student and Teacher be subclasses of User instead?
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

"""
Possible additional user attributes:
Profile page (a separate model?)

"""
