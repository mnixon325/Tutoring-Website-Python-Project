from django.contrib import admin
from .models import UploadedImage


@admin.register(UploadedImage)
class UserAdmin(admin.ModelAdmin):
    pass