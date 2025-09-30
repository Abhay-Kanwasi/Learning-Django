from django.urls import path, register_converter
from enroll import views
from enroll import convertor, views

register_converter(convertor.FourDigitConvertor, 'yyyy')

urlpatterns = [
    path('home/',views.home, name="home"),
    path('show/<int:my_id>/',views.show_details, name='detail'),
    path('show/<int:my_id>/<int:subid>',views.show_subdetails, name='subdetail'),
    path('session/<yyyy:year>/', views.show_session, name='session')
]
