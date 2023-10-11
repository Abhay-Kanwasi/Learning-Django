from django.shortcuts import render

from enroll.models import Student
from enroll.forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.

# def studentinfo(request):
#     stud = Student.objects.get(pk=1)   
#     return render(request, 'enroll/studetails.html', {'stud':stud})

# def showformdata(request):
#     fm = StudentRegistration(auto_id='some_%s', label_suffix='')
#     fm.order_fields(field_order=['email','name'])
#     return render(request, 'enroll/register.html', {'form':fm})


def thankyou(request):
    return render(request, 'enroll/sucess.html')

def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Form Validation")
            print('Name :', fm.cleaned_data['name'])
            print('Email :', fm.cleaned_data['email'])

            # method 1
            # return render(request, 'enroll/sucess.html',{'form':fm})

            # method 2
            return HttpResponseRedirect('/enroll/sucess/')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/register.html', {'form' : fm})