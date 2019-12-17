from rest_framework import serializers
from tutor.models import Tutor
from users.models import User


class TutorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Tutor
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')


class NotATutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')
        read_only_fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')