from django.urls import path
from enroll import views

urlpatterns = [
    path('home/',views.home, name="home"),
    path('show/<my_id>/',views.show_details, name='detail')
]
