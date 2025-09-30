from django.urls import path
from . import views

urlpatterns = [
    # path('stu/',views.studentinfo),
    # path('register/',views.showformdata),
    path('data/',views.showformdata),
    # path('facultycorner/',views.facultyform),
    # path('facultydelete/',views.facultydeleteform),
    path('staffdata/',views.showstaffdata)
    # path('sucess/', views.thankyou)
]
