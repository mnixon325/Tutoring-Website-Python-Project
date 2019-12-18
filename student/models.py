#Imports models from django.db
from django.db import models


#Student model for creating a student user
class Student(models.Model):
    #Defines structure of stored data
    #Defines owner as a OneToOneField, so each user can only have 1 student profile
    owner = models.OneToOneField('users.User', related_name='students', on_delete=models.CASCADE, primary_key=False)
    #Defines bio as a CharField with a max_length of 500 so the user can enter a descriptive bio
    bio = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    #Defines img_profile as a CharField so a profile picture can be uploaded
    img_profile = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    #Defines classes as a CharField so user can enter all of their classes
    classes = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")