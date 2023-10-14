from django.shortcuts import render

def home(request):
    return render(request, 'enroll/home.html')

# def show_details(request, my_id):
#     print(my_id)
#     return render(request, 'enroll/show.html',{'id':my_id}) 

def show_details(request,my_id):
    if my_id == 1:
        student = {'id':my_id, 'name':'Abhay Kanwasi'}
    if my_id == 2:
        student = {'id':my_id, 'name':'Abhay Bhardwaj'}
    if my_id == 3:
        student = {'id':my_id, 'name':'Aman Bisht'}
    return render(request, 'enroll/show.html',student)

def show_subdetails(request,my_id, subid):
    if my_id == 1 and subid==5:
        student = {'id':my_id, 'name':'Abhay Kanwasi', 'info':subid}
    if my_id == 2 and subid==9:
        student = {'id':my_id, 'name':'Abhay Bhardwaj', 'info':subid}
    if my_id == 3 and subid==3:
        student = {'id':my_id, 'name':'Aman Bisht', 'info':subid}
    return render(request, 'enroll/show.html',student)

def show_session(request, year):
    student = {'session' : year}
    return render(request, 'enroll/session.html', student)
