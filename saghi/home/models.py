from django.db import models
from datetime import datetime

class Tag(models.Model):
    tag_name = models.CharField(max_length=50,unique=True)
    tag_url = models.CharField(max_length=500,default="/search?q=")
    def __str__(self):
        return f"{self.tag_name}"
    
    def save(self,*args,**kwargs):
        if (self.tag_name not in  self.tag_url) and self.tag_name != "/search?q=":
            self.tag_url += self.tag_name
        super(Tag,self).save(*args,**kwargs)

class Actor(models.Model):
    actor = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return f"{self.actor}"

class Director(models.Model):
    director = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return f"{self.director}"

class Country(models.Model):
    country = models.CharField(max_length=70,unique=True)
    def __str__(self):
        return f"{self.country}"

class Resolution(models.Model):
    resolution = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return f"{self.resolution}"

class Movie(models.Model):
    title = models.CharField(max_length=300)
    tag = models.ManyToManyField(Tag,related_name="tag_rel_home",null=True, blank=True)
    country = models.ManyToManyField(Country,related_name="country_rel_home",null=True, blank=True)
    resolution = models.ManyToManyField(Resolution,related_name="resolution_rel_home",null=True, blank=True)
    actor = models.ManyToManyField(Actor, related_name="actor_rel_home",null=True, blank=True)
    director = models.ManyToManyField(Director,related_name="director_rel_home",null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    IMDB_point = models.FloatField()
    poster = models.ImageField(null=True, blank=True)
    publication = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title}"

class TypeDownload(models.Model):
    type = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.type}"

class download(models.Model):
    title = models.ManyToManyField(Movie,related_name="title_rel_home",null=True, blank=True)
    type = models.ManyToManyField(TypeDownload,related_name="type_rel_home",null=True, blank=True)
    quality = models.IntegerField(default=0)                                                         # کیفیت
    Volume = models.IntegerField(default=0)                                                          # حجم
    download_url = models.URLField(default="https://www.example.com/download",help_text="<h2>Enter a URL to download file</h2>")
    def __str__(self):
        return f"{self.title}|{self.type}|{self.quality}"
    