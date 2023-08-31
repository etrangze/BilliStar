from django.urls import path

from loginApp.views import login

urlpatterns = [
    path('login' , login),
]