from users.models import User
from users.serializers import UserSerializer

from rest_framework import permissions
from rest_framework import generics
from users.permissions import IsItselfOrReadOnly


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsItselfOrReadOnly,)