from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
]
