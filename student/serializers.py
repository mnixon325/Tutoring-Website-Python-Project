#Imports serializers from rest_framework and Student from the models file in student
from rest_framework import serializers
from student.models import Student

#Serializer for creating a student profile if user is a student
class StudentSerializer(serializers.ModelSerializer):
    #Defines owner as a read only field
    owner = serializers.ReadOnlyField(source='owner.username')

    #Meta class that defines which models and fields will be used in this serializer
    class Meta:
        #States that Student model will be used
        model = Student
        #Sets fields from the Student model that will be displayed
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'classes')

#Serializer that does not allow for creating a student profile if user is not a student
class NotAStudentSerializer(serializers.ModelSerializer):

    #Meta class that defines which models and fields will be used in this serializer
    class Meta:
        #States that Student model will be used
        model = Student
        #Sets fields from the Student model that will be displayed
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'classes')
        #Sets all the fields declared above as read only so they cannot be edited
        read_only_fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'classes')