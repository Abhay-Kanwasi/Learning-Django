from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'You loginned successfully!')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'user/home.html', {'form':form}) 