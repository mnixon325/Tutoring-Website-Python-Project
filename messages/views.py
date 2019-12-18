from rest_framework import generics

from messages.models import Message
from messages.serializers import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    """
    Defines the message list view from the generic Django API view.
    """
    queryset = Message.objects.all().order_by('-created')
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """Defines the message detail view."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
