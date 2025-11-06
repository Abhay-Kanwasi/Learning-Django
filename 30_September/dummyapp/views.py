from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    now = datetime.now()
    context = {
        'welcome message': 'Welcome to my Django site!',
        'current_time': str(now),
        'items' : [
            {'name' : 'Item1', 'description' : 'Item 1 description'},
            {'name' : 'Item2', 'description' : 'Item 2 description'},
            {'name' : 'Item3', 'description' : 'Item 3 description'},
            {'name' : 'Item4', 'description' : 'Item 4 description'},
        ],
        'user' : 'abhay',
        'condition' : True
    }
    print(['name'])
    return render(request, 'dummyapp/home.html', context=context)

def about(request):
    context = {
        'welcome message': 'Welcome to my Django site about page!',
        'current time': datetime.now(),
        'items' : [
            {'name' : 'Item1', 'description' : 'Item 1 description'},
            {'name' : 'Item2', 'description' : 'Item 2 description'},
            {'name' : 'Item3', 'description' : 'Item 3 description'},
        ]
    }
    return render(request, 'dummyapp/about.html', context)