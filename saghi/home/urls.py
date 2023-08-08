from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('movie/',views.movie_page),
]
