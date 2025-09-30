from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, HttpResponseRedirect
from django.conf import settings

from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm

def activateEmail(request, user, to_email):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'verification_email.html')
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, fm.cleaned_data.get('email'))
            messages.success(request, 'Account Created Successfully !')
            return render(request, 'signup.html', {'form':fm})
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form':fm})


def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username = uname, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request, 'please enter the correct details')
    else:    
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form':fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance= request.user)
                users = User.objects.all()
            else: 
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'Profile Updated !')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None 
        return render(request,'dashboard.html', {'name':request.user.username, 'form':fm, 'users':users})
    else:
        return render(request, 'dashboard.html')
    

def user_details(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditUserProfileForm(instance=pi)
        return render(request, 'userdetails.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')