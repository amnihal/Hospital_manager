from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url('view_emp/',views.Employees),
    path('post_emp/',views.postemp),
]