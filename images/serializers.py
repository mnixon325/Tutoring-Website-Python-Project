from rest_framework import serializers
from images.models import UploadedImage


class UploadedImageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UploadedImage
        fields = ('created', 'imagefile', 'user', 'id','path_to_image')
        read_only_fields = ('created', 'imagefile', 'user', 'id','path_to_image')