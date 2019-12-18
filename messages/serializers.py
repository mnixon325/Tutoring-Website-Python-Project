from rest_framework import serializers
from messages.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.CharField(max_length=120)
    receiver = serializers.CharField(max_length=120)

    class Meta:
        model = Message
        fields = ('url', 'id', 'created', 'sender', 'receiver', 'subject', 'content')
        read_only_fields = ('created', 'id')

