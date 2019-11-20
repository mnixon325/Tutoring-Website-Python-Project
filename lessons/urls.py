from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from lessons import views

urlpatterns = [
    path('lessons/', views.LessonList.as_view(), name="lesson-list"),
    path('lesson/<int:pk>/', views.LessonDetail.as_view(), name="lesson-detail"),
]

#urlpatterns = format_suffix_patterns(urlpatterns)