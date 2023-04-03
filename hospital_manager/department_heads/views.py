from django.shortcuts import render
from django.http import HttpResponse
from .models import Departmentheads
from .forms import posthead
# Create your views here.


def departmentheads(request):
    dict_dhead = {
        'dhead': Departmentheads.objects.all()
    }
    return render(request,'temp/head.html',dict_dhead)


    

