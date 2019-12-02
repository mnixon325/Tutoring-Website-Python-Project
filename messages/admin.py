from django.contrib import admin
from messages.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass