from django.shortcuts import render
from datetime import datetime, timedelta

def home(request):
    return render(request, 'home.html')

def setcookie(request):
    response = render(request, 'setcookie.html')
    response.set_cookie('name', 'abhay')
    return response

def getcookie(request):

    # method 1
    # name = request.COOKIES['name']

    # method 2
    name = request.COOKIES.get('name',"default value")

    return render(request, 'getcookie.html', {'name': name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response


def signed_set_cookie(request):
    response = render(request, 'setsignedcookie.html')
    response.set_signed_cookie('name', 'abhay', salt="nm", expires = datetime.utcnow()+timedelta(days=2))
    return response

def signed_get_cookie(request):
    name = request.get_signed_cookie('name', salt='nm')
    return render(request, 'getsignedcookie.html', {'name': name})
