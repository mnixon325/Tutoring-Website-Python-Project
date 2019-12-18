#Imports Student model from model file in student
from student.models import Student
#Imports StudentSerializer and NotAStudentSerializer serializers from serializer file in student
from student.serializers import StudentSerializer, NotAStudentSerializer
#Import permissions from rest_framework
from rest_framework import permissions
#Import generics from rest_framework
from rest_framework import generics
#Import IsOwnerOrReadOnly from permissions file of users
from users.permissions import IsOwnerOrReadOnly

#Class that defines StudentList view using APIView
class StudentList(generics.ListCreateAPIView):
    #Defines queryset of all objects of Student model
    queryset = Student.objects.all()
    #Based this function off of https://stackoverflow.com/questions/52081115/drf-object-level-permissions-check-for-single-field
    #Function that determines which Serializer view is displayed to the user depending on if they are a student or not
    def get_serializer_class(self):
        #If is_student field for current user is set to true, then displays StudentSerializer view
        if self.request.user.is_student:
            return StudentSerializer
        #If is_student field for current user is set to false, then displays NotAStudentSerializer view
        else:
            return NotAStudentSerializer
    #Defines permission class that uses permissions.IsAuthenticatedOrReadOnly
    #This permission makes sure the user is logged in before they can edit any fields
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #Overrides .perform_create method on student views to pass an 'owner' field along with the validated data from the
    #request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#Class that defines StudentDetail view using APIView
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    #Defines queryset of all objects of Student model
    queryset = Student.objects.all()
    #Uses the StudentSerializer for the view
    serializer_class = StudentSerializer
    #Defines permission class that uses permissions.IsAuthenticatedOrReadOnly
    #This permission makes sure the user is logged in before they can edit any fields. Also uses IsOwnerOrReadOnly,
    #which verifies the user is the owner of the profile before they can edit or delete it
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)