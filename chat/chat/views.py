from django.shortcuts import render
from django.http import JsonResponse
from .models import Conversation

def chat_view(request):
    conversations = Conversation.objects.all()
    return render(request, 'chat/chat.html', {'conversations': conversations})

def add_message(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        message = request.POST.get('message')
        Conversation.objects.create(user=user, message=message)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'fail'})