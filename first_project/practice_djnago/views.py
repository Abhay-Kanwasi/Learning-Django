from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def practice(request):
    return HttpResponse("<h2>Practice makes a man perfect</h2>")

