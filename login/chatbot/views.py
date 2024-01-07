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
            {"role":"system","content":"You are a historian, narrating history to a 10 year old, describe only in 50 words"},
            {"role":"user","content":prompt},
        ],
    )
    
    bot_response = response['choices'][0]['message']["content"]
    return bot_response  # Return the complete bot response text

from django.urls import reverse


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt  # Use this decorator for simplicity (handle CSRF protection properly in production)
def process_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('speechText')
        data=chat_with_gpt(prompt)
        print(data)
#        asyncio.run(speakText(data))
        response_data = {
            'prompt': prompt,
            'data': data
        }
        print("set to return")
        return JsonResponse(response_data)
        
import speech_recognition as sr
import pyttsx3
import pyttsx3
import asyncio
import requests
import pygame
from io import BytesIO

async def speakText(response):
    # engine = pyttsx3.init()
    # engine.setProperty('rate', 175)
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)
    
    # # Use await with an asyncio.sleep to simulate asynchronous behavior
    # engine.say(response)
    # engine.runAndWait()
    url = "https://api.elevenlabs.io/v1/text-to-speech/M8yHS9kJha5B58EgRBNL"

    querystring = {"optimize_streaming_latency":"1","output_format":"mp3_44100_96"}

    payload = {
        "model_id": "eleven_multilingual_v2",
        "text": response,
        "voice_settings": {
            "similarity_boost": 1,
            "stability": 1,
            "style": 1,
            "use_speaker_boost": True
        }
    }
    headers = {
        "xi-api-key": "8adc752bac062095fabfb8ba39ff7da8",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    if response.status_code == 200:
        # Save the audio content as an MP3 file
        with open("output_audio.mp3", "wb") as f:
            f.write(response.content)

        # Initialize Pygame mixer
        pygame.mixer.init()
        
        # Load the MP3 file
        pygame.mixer.music.load("output_audio.mp3")
        
        # Play the audio
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print("Error:", response.status_code)


    # Introduce a small delay (simulating asynchronous behavior)
    await asyncio.sleep(0.1)  # Adjust the delay time if needed
   

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


