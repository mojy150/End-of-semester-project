from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"],cd["email"],cd["password"])        
    else:
        form = UserRegistrationForm()
    return render(request,'signup.html',{"form":form})

def profile(request):
    return render(request,'panel.html')