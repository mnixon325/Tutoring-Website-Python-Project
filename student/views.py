from student.models import Student
from student.serializers import StudentSerializer, NotAStudentSerializer

from rest_framework import permissions
from rest_framework import generics
from users.permissions import IsOwnerOrReadOnly

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    #serializer_class = StudentSerializer
    def get_serializer_class(self):
        if self.request.user.is_student:
            return StudentSerializer
        else:
            return NotAStudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)