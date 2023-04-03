from django.urls import path,include
from departments import views
from django.conf.urls import url

urlpatterns = [
   
    url('dept/',views.departments),
   
]