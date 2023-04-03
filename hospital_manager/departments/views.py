from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments
# Create your views here.


def departments(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request,'temp/department.html',dict_dept)

