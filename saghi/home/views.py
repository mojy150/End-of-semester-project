from django.shortcuts import render
from home import models

def home(request):
    movie = models.Movie.objects.all()
    return render(request,'index.html',{'movies':movie})

def movie_page(request,movie_id):
    movie = models.Movie.objects.get(id=movie_id)
    return render(request,'movieDetails.html',{'movie':movie})