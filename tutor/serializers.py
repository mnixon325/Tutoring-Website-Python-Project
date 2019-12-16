from rest_framework import serializers
from tutor.models import Tutor


class TutorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tutor
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')