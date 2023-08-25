from django.shortcuts import render

def learn_django(request):
    cname = 'Django'
    duration = '4 Months'
    seats = 10
    django_details = {'name' : cname, 'duration' : duration, 'seats' : seats}
    return render
    