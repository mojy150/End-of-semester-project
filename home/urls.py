from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('movie/<int:movie_id>/',views.movie_page,name="movie"),
    path('search/',views.search,name="search"),
]
