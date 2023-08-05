from django.shortcuts import render
from home import models

def home(request):
    movie = models.Movie.objects.all()
    return render(request,'index.html',{'movies':movie})