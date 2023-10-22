from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect

from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !')
            fm.save()
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
                return HttpResponseRedirect('/profile/')
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
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated !')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
            else:
                fm = EditUserProfileForm(instance=request.user)
        return render(request,'profile.html', {'name':request.user.username, 'form':fm})
    else:
        return render(request, 'profile.html')