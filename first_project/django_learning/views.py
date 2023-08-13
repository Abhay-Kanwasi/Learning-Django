from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def learn_djnago(request):
    return HttpResponse('<h1> Hello Good Evening </h1>')

def learn_python(request):
    return HttpResponse('<h1>Python.. Python.. Python...</h1>')