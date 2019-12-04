from rest_framework import serializers
from messages.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.CharField()
    receiver = serializers.CharField()

    class Meta:
        model = Message
        fields = ('url', 'id', 'created', 'sender', 'receiver', 'content')
        read_only_fields = ('created', 'id')
