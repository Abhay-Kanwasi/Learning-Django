from django.shortcuts import render

# Create your views here.
def show_details(request):
    return render(request, 'enroll/show.html')
