from django.shortcuts import render
from datetime import datetime

def variable_passing(request):
    course_name = 'Django Practice'
    about_course = 'This is a django course where we learn about Django Template Language because django is independent in case of front end because it\'s have it\'s own front end system which is DTL and we can also integrate frontend\'s like React, Angular etc.\nLet\'s get started...'
    course_duration = '3 Months'
    available_seats = 100
    learn_django_details = {
        'Course_Name' : course_name, 
        'About' : about_course, 
        'Course_Duration' : course_duration, 
        'Available_Seats' : available_seats
        }
    return render (request,'course/variable_passing.html', learn_django_details)

def filters(request):
    return render (request, 'course/filters.html', {'name' : 'applying filter to this string to demonstrate filters in DTL', 'p1' : 56.24321, 'p2' : 56.00000, 'p3' : 56.37000})
    

def time(request):
    d = datetime.now()
    return render (request, "course/datetime.html", {'date' : d}) # We can't pass d because it takse dictionary as argument

def conditional(request):
    return render(request, "course/conditional.html", {'name': 'Abhay', 'age' : 20, 'mageclass' : 'nooby'})

def loop(request):
    student = {'names':['Abhay', 'Aman', 'Sohan', 'Mohan']}
    return render(request, 'course/loop.html', student)

def loop2(request):
    students = {
        'student1' : {'name' : 'Abhay', 'roll' : 1},
        'student2' : {'name' : 'Abhay2', 'roll' : 2},
        'student3' : {'name' : 'Abhay3', 'roll' : 3},
        'student4' : {'name' : 'Abhay4', 'roll' : 4},
    }
    students_dictionary = {'students' : students}

    # key value pair example
    # data = {'name' : 'Rahul', 'rollno' : 12}
    # return render(request, 'course/loop2.html','data' : data)

    return render(request, 'course/loop2.html',students_dictionary)
