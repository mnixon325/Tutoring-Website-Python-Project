from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'owner', 'created', 'description', 'img')

# class PostsSerializer(serializers.ModelSerializer):
#     #created = serializers.DateTimeField(auto_now_add=True)
#     description = serializers.CharField(max_length=500, required=False)
#     img = serializers.CharField(max_length=100, required=False)
#
#     def create(selfself, validated_data):
#         """
#         Create and return a new `Posts` instance, given the validated data
#         """
#         return Posts.objects.create_post(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Posts` instance, given the validated data
#         """
#         #instance.created = validated_data.get('created', instance.created)
#         instance.description = validated_data.get('description', instance.description)
#         instance.img = validated_data.get('img', instance.img)
#         instance.save()
#         return instance
#
#     class Meta:
#         model = Posts
#         fields = ('id', 'created', 'description', 'img')