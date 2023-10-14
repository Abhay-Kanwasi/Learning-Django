from django.shortcuts import render

def home(request):
    return render(request, 'enroll/home.html')

def show_details(request, my_id):
    print(my_id)
    return render(request, 'enroll/show.html',{'id':my_id}) 
