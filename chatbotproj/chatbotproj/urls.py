from django.contrib import admin
from django.urls import path, include
from chatbot import urls as chatbot_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(chatbot_urls)),
]
