from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("HELLO THIS IS A VIEW INSIDE MY_APP")
