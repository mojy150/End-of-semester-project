from django.db import models
from datetime import datetime

class Genre(models.Model):
    genre = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.genre}"

class Actor(models.Model):
    actor = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.actor}"

class Director(models.Model):
    director = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.director}"

class Movie(models.Model):
    title = models.CharField(max_length=300)
    genre = models.ManyToManyField(Genre,related_name="genre_rel_home")
    country = models.CharField(max_length=250)
    resolution = models.CharField(max_length=50)
    actor = models.ManyToManyField(Actor, related_name="actor_rel_home")
    director = models.ManyToManyField(Director,related_name="director_rel_home")
    description = models.TextField()
    IMDB_point = models.FloatField()
    # poster = 
    date = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title}"