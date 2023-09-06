from django.shortcuts import render

def django_fees(request):
    fees = {'course' : 1200}
    return render(request, 'fees/info.html', fees)