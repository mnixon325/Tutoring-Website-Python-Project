#Imports path from django.urls and views from student
from django.urls import path
from student import views

#Delares url patterns that define how the StudentList and StudentDetail pages will be accessed
urlpatterns = [
    path('students/', views.StudentList.as_view(), name="student-list"),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name="student-detail"),
]
