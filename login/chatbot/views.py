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


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import json
import io
@csrf_exempt  # Use this decorator for simplicity (handle CSRF protection properly in production)
def process_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('speechText')
        data=chat_with_gpt(prompt)
        print(data)
        asyncio.run(speakText(data))
        response_data = {
            'prompt': prompt,
            'data': data
        }
        print("set to return")
        return JsonResponse(response_data)
        
import speech_recognition as sr
import pyttsx3
import pygame
import pyttsx3
import asyncio

async def speakText(response):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    # Use await with an asyncio.sleep to simulate asynchronous behavior
    engine.say(response)
    engine.runAndWait()
    
    # Introduce a small delay (simulating asynchronous behavior)
    await asyncio.sleep(0.1)  # Adjust the delay time if needed

def takePrompt(audio_io):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_io) as source:
        audio = recognizer.record(source)

        try:
                # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return JsonResponse({'error': 'Google Web Speech API could not understand the audio'})
        except sr.RequestError:
            return JsonResponse({'error': 'Could not request results from Google Web Speech API'})    
            

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

