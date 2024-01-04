from django.urls import path
from . import views

urlpatterns = [
        path('chat/', views.chat, name='chat'),
        path('process_text/', views.process_text, name='process_text'),
]
