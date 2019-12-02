from lessons.models import Lesson
from lessons.serializers import LessonSerializer

from rest_framework import permissions
from rest_framework import generics

from messages.models import Message
from messages.serializers import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # def perform_create(self, serializer):
    #     serializer.save(sender=self.request.user)   # TODO: Probably change or delete.
    #     serializer.save()


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



"""
From https://stackoverflow.com/questions/32687461/how-to-create-a-user-to-user-message-system-using-django

Message.objects.filter(receiver = request.user)
Message.objects.filter(sender = request.user
"""
