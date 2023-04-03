from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'temp/home.html')

def admin(request):
    return render(request,'temp/admin.html')

