from django.shortcuts import render

from enroll.models import Student, Faculty, Staff
from enroll.forms import StudentRegistration, FacultyRegistration, StaffRegistrations
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
            sid = fm.cleaned_data['student_id']
            name = fm.cleaned_data['student_name']
            email = fm.cleaned_data['student_email']
            password = fm.cleaned_data['student_password']
            comment = fm.cleaned_data['comment']
            student = Student(student_id=sid,student_name=name, student_email=email, student_password=password, comment=comment)
            student.save()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/register.html', {'form':fm})

#######################################################################################

# def facultyform(request):
#     if request.method == "POST":
#         fm = FacultyRegistration(request.POST)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             email = fm.cleaned_data['email']
#             subject = fm.cleaned_data['subjects']
#             fid = fm.cleaned_data['fid'] 
#             slogan = fm.cleaned_data['slogan']
#             faculty = Faculty(faculty_name = name, faculty_email = email, faculty_subjects=subject, faculty_id = fid, faculty_slogan = slogan)
#             faculty.save()
#     else:
#         fm = FacultyRegistration()
#     return render(request, 'enroll/faculty.html',{'form':fm})

# ###################################################################################
# def facultydeleteform(request):
#     if request.method == "POST":
#         fm = FacultyRegistration(request.POST)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             email = fm.cleaned_data['email']
#             subject = fm.cleaned_data['subjects']
#             fid = fm.cleaned_data['fid'] 
#             slogan = fm.cleaned_data['slogan']
#             # delete by id
#             faculty = Faculty(id=1)
#             faculty.delete()
#     else:
#         fm = FacultyRegistration()
#     return render(request, 'enroll/facultyd.html',{'form':fm})

###########################################################################

def showstaffdata(request):
    if request.method == "POST":
        fm = StaffRegistrations(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['staff_name']
            email = fm.cleaned_data['staff_email']
            subject = fm.cleaned_data['staff_subjects']
            fid = fm.cleaned_data['staff_id'] 
            slogan = fm.cleaned_data['staff_slogan']
            
            staff = Staff(staff_name=name, staff_email=email, staff_subjects=subject, staff_id=fid, staff_slogan=slogan)
            staff.save()
    else:
        fm = StaffRegistrations()
    return render(request, 'enroll/staff.html', {'form': fm})