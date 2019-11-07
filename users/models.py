from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    description = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    img_profile = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")