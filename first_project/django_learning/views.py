from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2> Home </h2></br><h2> Python </h2>')

def learn_djnago(request):
    return HttpResponse('<h1> Hello Good Evening </h1>')

def learn_python(request):
    return HttpResponse('<h1>Python.. Python.. Python...</h1>')

def learn_github(request):
    year = 2023
    a = f'It is essential bro to learn github by {year}'
    return HttpResponse(a)