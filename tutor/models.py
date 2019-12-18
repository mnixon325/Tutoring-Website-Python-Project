#Imports models from django.db
from django.db import models


#Tutor model for creating a Tutor user
class Tutor(models.Model):
    #Defines structure of stored data
    #Defines owner as a OneToOneField, so each user can only have 1 tutor profile
    owner = models.OneToOneField('users.User', related_name='tutors', on_delete=models.CASCADE, primary_key=False)
    #Defines bio as a CharField with a max_length of 500 so the user can enter a descriptive bio
    bio = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    #Defines img_profile as a CharField so a profile picture can be uploaded
    img_profile = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    #Defines qualifications as a CharField with a max_length of 500 so the user can list all their qualifications
    qualifications = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    #Defines travelPolicy as a CharField with a max_length of 500 so the user can enter their travelPolicy
    travelPolicy = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    #Defines hourlyRate as a CharField with a max_length of 100 so the user can enter what their hourlyRate is
    hourlyRate = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")