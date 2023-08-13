from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def learn_djnago(request):
    return HttpResponse('<h1> Hello Good Evening </h1>')