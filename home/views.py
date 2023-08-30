from django.shortcuts import render
from home import models

def home(request):
    movie = models.Movie.objects.all()
    return render(request,'index.html',{'movies':movie})

def movie_page(request,movie_id):
    movie = models.Movie.objects.get(id=movie_id)
    downloads = models.Download.objects.filter(title=movie)  # فیلتر کردن بر اساس فیلم مورد نظر
    return render(request, 'movieDetails.html', {'movie': movie, 'downloads': downloads})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        movie = models.Movie.objects.filter(title__contains=search)
        return render(request,'search.html',{'search':search,'movies':movie})
    else:
        return render(request,'search.html')