from django.shortcuts import render,HttpResponse,redirect,reverse
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from logapp.forms import LoginForm,RegisterForm
from logapp.models import Login,Register
from django.contrib import messages

def RegisterPage(request):
    if request.method=="POST":
        registerForm=RegisterForm(request.POST)
        if registerForm.is_valid():
            keyOne=registerForm.cleaned_data.get('pass1')
            keyTwo=registerForm.cleaned_data.get('pass2')
            username=registerForm.cleaned_data.get('email')
            email=Register.objects.filter(email=username).exists()
            if keyOne==keyTwo and email==False and len(keyOne)>=8:
                login=Login(email=username,password=keyOne)
                registerForm.save()
                login.save()
                return redirect('loginPage')
            else:
                return HttpResponse("Registerd already")
    context={'form':RegisterForm}
    return render(request,'logapp/register.html',context)

# Create your views here.
def LoginPage(request):
    if request.method=='POST':
        loginForm=LoginForm(request.POST)
        if loginForm.is_valid():
            print('clean')
            username=loginForm.cleaned_data.get('email')
            password=loginForm.cleaned_data.get('password')
            #emailExists=Login.objects.filter(email=username).exists()
            try:
                user=Login.objects.get(email=username)
                print('got things')
                if user.password==password:
                    print('got it')
                    return redirect(reverse('chat'))
                else:
                    messages.error(request, 'Incorrect Credentials')  # Add error message
                    context = {"form": loginForm}
                    return render(request, 'logapp/login.html', context)
            except:
                return HttpResponse("Email doesn't exists")
    context={"form":LoginForm}
    return render(request,'logapp/login.html',context)    
    

        

