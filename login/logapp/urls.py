from django.urls import path
from . import views

urlpatterns = [
    path('',views.LoginPage,name='loginPage'),
    path('register',views.RegisterPage,name='RegisterPage')
]
