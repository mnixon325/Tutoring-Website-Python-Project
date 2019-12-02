from django.urls import path
from messages import views

urlpatterns = [
    path('messages/', views.MessageList.as_view(), name="message-list"),
    path('message/<int:pk>/', views.MessageDetail.as_view(), name="message-detail"),
]

#urlpatterns = format_suffix_patterns(urlpatterns)