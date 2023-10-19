from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# signup page
def user_signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully!")
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'login/signup.html', {'form': fm})

# login page
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'login/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')