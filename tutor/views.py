#Imports Tutor model from model file in tutor
from tutor.models import Tutor
#Imports TutorSerializer and NotATutorSerializer serializers from serializer file in tutor
from tutor.serializers import TutorSerializer, NotATutorSerializer
#Import permissions from rest_framework
from rest_framework import permissions
#Import generics from rest_framework
from rest_framework import generics
#Import IsOwnerOrReadOnly from permissions file of users
from users.permissions import IsOwnerOrReadOnly

#Class that defines TutorList view using APIView
class TutorList(generics.ListCreateAPIView):
    #Defines queryset of all objects of Tutor model
    queryset = Tutor.objects.all()
    #Based this function off of https://stackoverflow.com/questions/52081115/drf-object-level-permissions-check-for-single-field
    #Function that determines which Serializer view is displayed to the user depending on if they are a tutor or not
    def get_serializer_class(self):
        #If is_tutor field for current user is set to true, then displays TutorSerializer view
        if self.request.user.is_tutor:
            return TutorSerializer
        #If is_tutor field for current user is set to false, then displays NotATutorSerializer view
        else:
            return NotATutorSerializer
    #Defines permission class that uses permissions.IsAuthenticatedOrReadOnly
    #This permission makes sure the user is logged in before they can edit any fields
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #Overrides .perform_create method on tutor views to pass an 'owner' field along with the validated data from the
    #request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#Class that defines TutorDetail view using APIView
class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
    #Defines queryset of all objects of Tutor model
    queryset = Tutor.objects.all()
    #Uses the TutorSerializer for the view
    serializer_class = TutorSerializer
    #This permission makes sure the user is logged in before they can edit any fields. Also uses IsOwnerOrReadOnly,
    #which verifies the user is the owner of the profile before they can edit or delete it
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)