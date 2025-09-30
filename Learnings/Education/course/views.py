from django.shortcuts import render

def learn_django(request):
    names = {'name' : 'abhay'}
    return render(request, 'course/info.html', names)