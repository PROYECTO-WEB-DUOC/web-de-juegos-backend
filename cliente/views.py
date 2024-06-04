from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'cliente/index.html', context)


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