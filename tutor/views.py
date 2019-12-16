from tutor.models import Tutor
from tutor.serializers import TutorSerializer, NotATutorSerializer

from rest_framework import permissions
from rest_framework import generics
from users.permissions import IsOwnerOrReadOnly
from users.permissions import IsTutorOrReadOnly

class TutorList(generics.ListCreateAPIView):
    queryset = Tutor.objects.all()
    #serializer_class = TutorSerializer
    def get_serializer_class(self):
        #if self.action == 'create':
        if self.request.user.is_tutor:
            return TutorSerializer
        else:
            return NotATutorSerializer
        #return super().get_serializer_class()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)