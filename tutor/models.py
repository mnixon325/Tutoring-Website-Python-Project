from django.db import models

# Create your models here.

class Tutor(models.Model):
    owner = models.OneToOneField('users.User', related_name='tutors', on_delete=models.CASCADE, primary_key=False)
    bio = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    img_profile = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    qualifications = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    travelPolicy = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    hourlyRate = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")