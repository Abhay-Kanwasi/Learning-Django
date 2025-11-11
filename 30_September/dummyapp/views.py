from datetime import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import CustomUser

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

def register_default_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            return redirect('home')
        except Exception as error:
            return render(request, 'dummyapp/profile.html', {'error': error})
    return render(request, 'dummyapp/profile.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('home')
        else:
            print('Login failed')
    return render(request, 'dummyapp/login.html')


def user_profile(request):
    user = CustomUser.objects.get(id=1)
    print(user)

    print(f'get user display {user.get_display_name()}')
    print(f'has premium access {user.has_premium_access()}')
    context = {
        'user' : user,
        'full_name' : user.get_full_name(),
        'email' : user.email,
        'username' : user.username,
        'last_login' : user.last_login,
        'date_joined' : user.date_joined,
        'phone_number' : user.phone_number,
    }
    print(context)
    return render(request, 'dummyapp/profile.html', context)