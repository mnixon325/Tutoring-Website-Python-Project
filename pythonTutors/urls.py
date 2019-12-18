"""pythonTutors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import include
from pythonTutors import views

# Defines all the relevant url patterns (mostly derived from models) for Python Tutors.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('lessons.urls')),
    path('', views.api_root),
    path('', include('messages.urls')),
    path('', include('postman.urls')),
    path('', include('student.urls')),
    path('', include('tutor.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]
