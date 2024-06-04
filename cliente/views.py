from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'cliente/index.html', context)


def gow(request):
    context={}
    return render(request, 'cliente/Juegos/gow.html', context)