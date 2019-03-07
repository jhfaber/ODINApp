from django.shortcuts import render
from django.http import HttpResponse

from datasource import source

# Create your views here.

def index(request):
    data = source.table()
    print(type(data))
    
    context = {
        'data' : data
        
    }
    return render(request,'template/inicio.html',context)


def gestionar_alertas(request):
    return render(request, 'alertasTemplates')