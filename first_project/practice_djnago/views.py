from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def practice(request):
    return render(request, "practice_django.html")

