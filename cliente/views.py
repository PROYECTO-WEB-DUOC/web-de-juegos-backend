from django.shortcuts import render
from .models import  Cliente,Genero
from . import forms
# Create your views here.

def index(request):
    context={}
    return render(request, 'cliente/index.html', context)

def crud(request):
    clientes=Cliente.objects.all()
    context={'clientes': clientes}
    return render(request, 'cliente/crud.html', context)


def clientesAdd(request):
    generos=Genero.objects.all()
    context={'generos':generos}
    return render(request,'cliente/crud.html', context)

def gow(request):
    context={}
    return render(request, 'cliente/Juegos/gow.html', context)

def spider(request):
    context={}
    return render(request, 'cliente/Juegos/spider.html', context)

def bloodborne(request):
    context={}
    return render(request, 'cliente/Juegos/bloodborne.html', context)

def dmc(request):
    context={}
    return render(request, 'cliente/Juegos/dmc.html', context)

def ps5(request):
    context={}
    return render(request, 'cliente/Categorias/ps5.html', context)

def ps4(request):
    context={}
    return render(request, 'cliente/Categorias/ps4.html', context)

def pc(request):
    context={}
    return render(request, 'cliente/Categorias/pc.html', context)

def crearc(request):
    context={}
    return render(request, 'cliente/Registros/crearc.html', context)

def registro(request):
    context={}
    return render(request, 'cliente/Registros/registro.html', context)