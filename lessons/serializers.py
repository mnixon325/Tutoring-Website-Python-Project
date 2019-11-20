from rest_framework import serializers
from lessons.models import Lesson


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Lesson
        fields = ('url', 'id', 'owner', 'created', 'description', 'img')
