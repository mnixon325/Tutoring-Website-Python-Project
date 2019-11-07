from rest_framework import serializers
from users.models import User
from posts.models import Post
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ('url', 'id', 'password', 'username', 'first_name', 'last_name', 'email', 'description', 'img_profile', 'posts')
        write_only_fields = ('password',)