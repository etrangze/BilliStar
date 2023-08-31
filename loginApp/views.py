from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def login(request):
    return HttpResponse("로그인페이지 입니다.")