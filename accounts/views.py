from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

from django.contrib import messages
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        user_name=request.POST['uname']
        password=request.POST['psw']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")

    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['u_name']
        email=request.POST['email']
        password=request.POST['psw']
        password_r=request.POST['psw-repeat']

        if password==password_r:
            if User.objects.filter(username=user_name).exists():
                
                return HttpResponse('Username already exists')
            elif User.objects.filter(email=email).exists():
            
                return HttpResponse('Email already exists')
            else:
                user = User.objects.create_user(username=user_name, password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('User Created')
                return redirect("login")
        else:
            return HttpResponse('password not matching')
      
    else:        
        return render(request,'registration.html')