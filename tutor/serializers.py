from rest_framework import serializers
from tutor.models import Tutor
from users.models import User


class TutorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # obj = User.objects.first()
    # field_object = User._meta.get_field('is_tutor')
    # field_value = field_object.value_from_object(obj)
    # if field_value == 'false':
    #     bio = serializers.RelatedField(read_only=True)
    #     qualifications = serializers.RelatedField(read_only=True)
    #     travelPolicy = serializers.RelatedField(read_only=True)
    #     hourlyRate = serializers.RelatedField(read_only=True)
    # elif field_value == 'true':
    #     bio = serializers.RelatedField(read_only=False)
    #     qualifications = serializers.RelatedField(read_only=False)
    #     travelPolicy = serializers.RelatedField(read_only=False)
    #     hourlyRate = serializers.RelatedField(read_only=False)
    # if 'owner.is_tutor' == 'true':
    #     bio = serializers.RelatedField(read_only=True)
    #     qualifications = serializers.RelatedField(read_only=True)
    #     travelPolicy = serializers.RelatedField(read_only=True)
    #     hourlyRate = serializers.RelatedField(read_only=True)
    class Meta:
        model = Tutor
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')
        #field_name = 'is_tutor'
        # obj = User.objects.first()
        # field_object = User._meta.get_field('is_tutor')
        # field_value = field_object.value_from_object(obj)
        # #if field == 'true':
        # if field_value == False:
        #     read_only_fields = ('bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')
        # else:
        #     write_only_fields = ('bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')


class NotATutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')
        read_only_fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'qualifications', 'travelPolicy', 'hourlyRate')