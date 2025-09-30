from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# signup page
def user_signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully!")
            fm.save()
            return HttpResponseRedirect('/login/')
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

# Change password withour old password
def user_changepassword(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) # so the session will be maintained as we know for going to profile we need to logged in but if we directly go for profile it will send us to login page so we need something which update our session and tells django that we user change his password and this user is authenticated. 
                messages.success(request, 'Password Changed Successfully!')
                return HttpResponseRedirect('/profile/')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'login/changepassword.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')    
    
# Change password without old password
def user_changepassword1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password successfully changed!")
                return HttpResponseRedirect('/profile/')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'login/changepassword1.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')
    
def show_userprofile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, "Your profile updated successfully !")
                fm.save()
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request, 'login/showprofile.html', {'name':request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/')