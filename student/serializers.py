from rest_framework import serializers
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'classes')

class NotAStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'classes')
        read_only_fields = ('url', 'id', 'owner', 'bio', 'img_profile', 'classes')