from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "IMDB_point", "duration"]
    

admin.site.register(Movie,MovieAdmin)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Country)
admin.site.register(Resolution)