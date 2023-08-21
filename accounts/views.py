from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd["username"],password=cd["password"])
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request,'username or password is wrong','warning')
    else:
        form = UserLoginForm()
    return render(request,'login.html',{"form":form})

def user_logout(request):
    logout(request)
    return redirect("home")

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"],cd["email"],cd["password"])
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request,'signup.html',{"form":form})

def profile(request):
    return render(request,'panel.html')