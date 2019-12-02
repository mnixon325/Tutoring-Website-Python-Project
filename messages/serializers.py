from rest_framework import serializers
from messages.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.ReadOnlyField(source='user.username')
    receiver = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Message
        fields = ('url', 'id', 'created', 'sender', 'receiver', 'content')
        read_only_fields = ('created', 'content', 'sender', 'receiver', 'id')
