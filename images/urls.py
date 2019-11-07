from django.conf.urls import url
from django.urls import path

from images import views


urlpatterns = [
    path('image/upload/', views.UploadedImagesView.as_view(), name='image-upload'),
]