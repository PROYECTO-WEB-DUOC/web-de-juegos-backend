from django.shortcuts import render
from .models import  Cliente,Genero,Juegos
from .forms import ClienteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    juegos=Juegos.objects.all()
    context={'juegos':juegos}
    return render(request, 'cliente/index.html', context)

def crud(request):
    clientes=Cliente.objects.all()
    context={'clientes': clientes}
    return render(request, 'cliente/crud.html', context)


def ps5(request):
    juegoss=Juegos.objects.all()
    context={'juegoss':juegoss}
    return render(request, 'cliente/Categorias/ps5.html', context)

def ps4(request):
    juegoss=Juegos.objects.all()
    context={'juegoss':juegoss}
    return render(request, 'cliente/Categorias/ps4.html', context)

def pc(request):
    juegoss=Juegos.objects.all()
    context={'juegoss':juegoss}
    return render(request, 'cliente/Categorias/pc.html', context)

def crearc(request):
    if request.method != "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'cliente/Registros/crearc.html', context)
    else:
        #es un post por lo tanto se guardan los datos en la tabla
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        apellido_paterno=request.POST["apellido"]
        genero=request.POST["genero"]
        email=request.POST["correo"]
        contraseña=request.POST["contraseña"]
        objgenero=Genero.objects.get(idgenero=genero)

        obj=Cliente.objects.create(rut=rut,
                                   nombre=nombre,
                                    apellido_paterno= apellido_paterno,
                                    id_genero=objgenero,
                                    email=email,
                                    contraseña=contraseña)
        obj.save()
        context={"mensaje": "Datos grabados"}
        user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=contraseña,
                    first_name=nombre,
                    last_name=apellido_paterno
                )
        user.save()
        return render(request,'cliente/Registros/crearc.html', context)
def registro(request):
    context={}
    return render(request, 'cliente/Registros/registro.html', context)





def game(request,idjuego):
        juegos=Juegos.objects.get(idjuego=idjuego)
        context={'juegos':juegos}
        return render(request,'cliente/Juegos/game.html',context)
   
    