from django.shortcuts import redirect, render,HttpResponse
from chatbot.forms import ChatForm
from chatbot.models import ChatMessage
from django.http import JsonResponse  # Import JsonResponse

# Create your views here.
import openai

openai.api_key="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"
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role":"system","content":"You are a historian, teaching history to a 10 year old"},
            {"role":"user","content":prompt},
        ],
    )
    
    bot_response = response['choices'][0]['message']["content"]
    return bot_response  # Return the complete bot response text

from django.urls import reverse

# ... (your other imports and code)

def chat(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['content']

            ChatMessage.objects.create(content=user_input, is_user=True)

            response = chat_with_gpt(user_input)
            ChatMessage.objects.create(content=response, is_user=False)

            return JsonResponse({'content': response})  # Return bot's response as JSON

            #return redirect(reverse("chat"))  # Redirect to the same view 'chat'
    else:
        form = ChatForm()

    chat_messages = ChatMessage.objects.all().order_by('timestamp')
    return render(request, 'chatbot/chat.html', {'form': form, 'chat_messages': chat_messages})

from django.http import JsonResponse
from .models import ChatMessage

