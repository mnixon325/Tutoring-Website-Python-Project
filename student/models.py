from django.db import models

# Create your models here.

class Student(models.Model):
    owner = models.OneToOneField('users.User', related_name='students', on_delete=models.CASCADE, primary_key=False)
    #owner = models.ForeignKey('users.User', related_name='students', on_delete=models.CASCADE, null=False)
    bio = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    img_profile = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    classes = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    #qualifications = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    #travelPolicy = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    #hourlyRate = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")