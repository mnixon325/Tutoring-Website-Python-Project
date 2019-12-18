#Imports path from django.urls and views from tutor
from django.urls import path
from tutor import views

#Delares url patterns that define how the TutorList and TutorDetail pages will be accessed
urlpatterns = [
    path('tutors/', views.TutorList.as_view(), name="tutor-list"),
    path('tutor/<int:pk>/', views.TutorDetail.as_view(), name="tutor-detail"),
]
