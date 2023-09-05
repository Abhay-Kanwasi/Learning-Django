from django.urls import path
from . import views

urlpatterns = [
    path("variable_passing/",views.variable_passing),    
    path("filters/",views.filters),   
    path("filters/date", views.time), # we can make url according to us
    path('conditional/', views.conditional),
]