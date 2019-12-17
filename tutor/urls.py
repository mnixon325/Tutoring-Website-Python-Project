from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from tutor import views

urlpatterns = [
    path('tutors/', views.TutorList.as_view(), name="tutor-list"),
    path('tutor/<int:pk>/', views.TutorDetail.as_view(), name="tutor-detail"),
]

#urlpatterns = format_suffix_patterns(urlpatterns)