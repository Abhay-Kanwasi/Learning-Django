from django.urls import path
from . import views

urlpatterns = [
    # path('stu/',views.studentinfo),
    # path('register/',views.showformdata),
    path('data/',views.showformdata),
    # path('sucess/', views.thankyou)
]
