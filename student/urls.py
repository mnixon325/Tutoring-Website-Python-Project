from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from student import views

urlpatterns = [
    path('students/', views.StudentList.as_view(), name="student-list"),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name="student-detail"),
]

#urlpatterns = format_suffix_patterns(urlpatterns)