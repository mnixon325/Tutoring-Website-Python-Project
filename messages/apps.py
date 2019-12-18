from django.apps import AppConfig


class MessagesConfig(AppConfig):
    name = 'messages'
    label = 'messages_app'      # Needed to change the label since 'messages' is too generic a name.
