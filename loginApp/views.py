from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def login(request):
    return render(request, "loginApp/hello_world.html")



