from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    content=models.TextField()
    is_user=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)