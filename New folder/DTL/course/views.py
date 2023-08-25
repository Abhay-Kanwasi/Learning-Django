from django.shortcuts import render

def learn_django(request):
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
    return render (request,'course/courseone.html', learn_django_details)
