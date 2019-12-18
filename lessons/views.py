from lessons.models import Lesson
from lessons.serializers import LessonSerializer

from rest_framework import permissions
from rest_framework import generics
from lessons.permissions import IsOwnerOrReadOnly


class LessonList(generics.ListCreateAPIView):
    """
    Extends the generic API list view class to view all lessons on the site.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Extends a generic API view class to view the details of a single lesson.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
