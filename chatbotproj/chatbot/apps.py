from django.apps import AppConfig
from .training import train_chatbot


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
    
    def ready(self):
        from .chatbot_instance import chatbot
        train_chatbot(chatbot)
