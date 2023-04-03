from django.urls import path,include
from temp import views
from django.conf.urls import url


urlpatterns = [
    url('home/',views.home),
    url('admin/',views.admin),
    
]