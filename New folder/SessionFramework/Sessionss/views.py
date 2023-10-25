from django.shortcuts import render
from datetime import datetime, timedelta
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def setsession(request):
   # all the set data will be added in same session
   request.session['name'] = 'Abhay'
   request.session['lname'] = 'Kanwasi'
   return render(request, 'setsession.html')

def getsession(request):
    # name = request.session['name'] # give the key to know the value
    name = request.session.get('name', 'Alex')
    lname = request.session.get('lname', '4617P')
    return render(request, 'getsession.html', {'name':name, 'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['lname']
    return render(request, 'delsession.html')
    

