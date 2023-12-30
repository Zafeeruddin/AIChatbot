from django import forms
from chatbot.models import ChatMessage
class ChatForm(forms.ModelForm):
    class Meta:
        model=ChatMessage
        fields={'content'}