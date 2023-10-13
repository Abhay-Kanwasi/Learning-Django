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

#############################################################################

# def thankyou(request):
#     return render(request, 'enroll/sucess.html')

# def showformdata(request):
#     if request.method == "POST":
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             print("Form Validation")
#             print('Name :', fm.cleaned_data['name'])
#             print('Email :', fm.cleaned_data['email'])

#             # method 1
#             # return render(request, 'enroll/sucess.html',{'form':fm})

#             # method 2
#             return HttpResponseRedirect('/enroll/sucess/')
#     else:
#         fm = StudentRegistration()
#     return render(request, 'enroll/register.html', {'form' : fm})

###################################################################################

# def showformdata(request):
#     if request.method == "POST":
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             print('Form Validation')
#             print("Name ", fm.cleaned_data['name'])
#             # print("Roll_number ", fm.cleaned_data['roll_number']) 
#             print("price ", fm.cleaned_data['price'])
#             print("Rate ", fm.cleaned_data['rate'])
#             print("Comment ", fm.cleaned_data['comment'])
#             print("Email ", fm.cleaned_data['email'])
#             print("Website ", fm.cleaned_data['website'])
#             print("Password ", fm.cleaned_data['password'])
#             print("Description ", fm.cleaned_data['description'])
#             print("Feedback ", fm.cleaned_data['feedback'])
#             print("Notes ", fm.cleaned_data['notes'])
#             print("Agree ", fm.cleaned_data['agree'])
#         else:
#             fm = StudentRegistration()
#     return render(request, 'enroll/register.html', {'form' : fm})

###################################################################################

def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Name ", fm.cleaned_data['name'])
            print("Email ", fm.cleaned_data['email'])
            print("Password", fm.cleaned_data['password'])
            print("Password (again)", fm.cleaned_data['rpassword'])
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/register.html', {'form':fm})

#######################################################################################