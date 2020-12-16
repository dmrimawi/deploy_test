from django.urls import path
from . import views


urlpatterns = [
    path('', views.reg_or_login),
    path('register', views.register),
    path('welcome', views.welcome),
    path('logout', views.logout),
    path('login', views.login),
]
