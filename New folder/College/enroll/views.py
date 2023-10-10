from django.shortcuts import render

from enroll.models import Student
from enroll.forms import StudentRegistration

# Create your views here.

def studentinfo(request):
    stud = Student.objects.get(pk=1)   
    return render(request, 'enroll/studetails.html', {'stud':stud})

def showformdata(request):
    fm = StudentRegistration(auto_id='some_%s', label_suffix='')
    fm.order_fields(field_order=['email','name'])
    return render(request, 'enroll/register.html', {'form':fm})