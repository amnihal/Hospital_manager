from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeAdd

# Create your views here.




def postemp(request):
    if request.method == 'POST':
        form = EmployeeAdd(request.POST)
        if form.is_valid():
            form.save()
    form = EmployeeAdd()
    dict_form={
        'form': form
    }
    return render(request,'temp/addemployee.html',dict_form)


def Employees(request):
    dict_emp = {
        'empl': Employee.objects.all()
    }
    return render(request,'temp/employee.html',dict_emp)