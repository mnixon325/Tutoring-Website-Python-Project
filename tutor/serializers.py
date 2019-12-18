#Imports serializers from rest_framework and Tutor from the models file in tutor
from rest_framework import serializers
from tutor.models import Tutor

#Serializer for creating a tutor profile if user is a tutor
class TutorSerializer(serializers.ModelSerializer):
    #Defines owner as a read only field
    owner = serializers.ReadOnlyField(source='owner.username')

    #Meta class that defines which models and fields will be used in this serializer
    class Meta:
        #States that Tutor model will be used
        model = Tutor
        #Sets fields from the Tutor model that will be displayed. Since these fields are not set to readOnly, they
        #can all be written to (except owner which is set as a ReadOnlyField above)
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')

#Serializer for viewing tutor profiles if user is not a tutor
class NotATutorSerializer(serializers.ModelSerializer):

    #Meta class that defines which models and fields will be used in this serializer
    class Meta:
        #States that Tutor model will be used
        model = Tutor
        #Sets fields from the Tutor model that will be displayed
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')
        #Sets all the fields declared above as read only so they cannot be edited, only viewed
        read_only_fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')