from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    lessons = serializers.HyperlinkedRelatedField(many=True, view_name='lesson-detail', read_only=True)

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ('url', 'id', 'password', 'username', 'first_name', 'last_name', 'email', 'description',
                  'img_profile', 'is_student', 'is_tutor', 'lessons')
        write_only_fields = ('password',)
