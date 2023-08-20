from django.shortcuts import render


# Create your views here.
def course_name(request):
    course = ("Django",)
    duration = ("6 months",)
    seats = 10
    django_details = {"name": course, "duration": duration, "seats": seats}
    return render(request, "DTF/courseone.html", django_details)
