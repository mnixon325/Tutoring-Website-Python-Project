from rest_framework import serializers
from lessons.models import Lesson


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Allows the use of hyperlinks to represent lesson-user relationships.
    """
    tutor = serializers.CharField(max_length=120)
    student = serializers.CharField(max_length=120)
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Lesson
        fields = ('url', 'id', 'creator', 'tutor', 'student', 'created', 'date_time', 'completed', 'subject')
        read_only_fields = ('created', 'id')
