from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_instance import chatbot

def home(request):
    return render(request, 'chatbot/home.html')

def get_response(request):
    user_message = request.GET.get('message')
    response = chatbot.get_response(user_message)
    return JsonResponse({'response': str(response)})
