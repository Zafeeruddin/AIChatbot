from django.db import models

# Create your models here.

class Register(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    email=models.EmailField()
    pass1=models.CharField(max_length=128)
    pass2=models.CharField(max_length=128)

class Login(models.Model):
    email=models.EmailField(default='mohammed.xafeer@gmail.com')
    password=models.CharField(max_length=100)
