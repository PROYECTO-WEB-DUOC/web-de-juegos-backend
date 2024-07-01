from django.shortcuts import render
from .models import  Cliente,Genero,Juegos,Categoria_juegos,Carrousel_2025,Carrito
from .forms import ClienteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.forms import ValidationError


# Create your views here.

def index(request):
    carrousel=Carrousel_2025.objects.all();
    juegos=Juegos.objects.all()
    cliente=Cliente.objects.all()
    
    context={'juegos':juegos,'carrousel':carrousel,'cliente':cliente}
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
            
            existe=Cliente.objects.filter(rut=rut).exists()
            existe2=Cliente.objects.filter(email=email).exists()
            if existe or existe2:
                generos=Genero.objects.all()
                messages.error(request,"Error al registrarse")
                context={'generos':generos}
                return render(request, 'cliente/Registros/crearc.html', context)

            
        
            user = User.objects.create_user(
                        username=email,
                        email=email,
                        password=contraseña,
                        first_name=nombre,
                        last_name=apellido_paterno
                    )
            user.save()
            obj=Cliente.objects.create(
                                    user=user,
                                    rut=rut,
                                    nombre=nombre,
                                        apellido_paterno= apellido_paterno,
                                        id_genero=objgenero,
                                        email=email,
                                        contraseña=contraseña)
            obj.save()
            context={"mensaje": "Datos grabados"}
            carrito = Carrito.objects.create(
                        correo_cliente=email,
                    )
            carrito.save()
            messages.success(request,"te has registrado")
            return render(request,'cliente/Registros/crearc.html', context)
   

def registro(request):
    context={}
    return render(request, 'cliente/Registros/registro.html', context)





def game(request,idjuego):
        juegos=Juegos.objects.get(idjuego=idjuego)
        categorias = Categoria_juegos.objects.filter(idcategoria=juegos.id_categoria.idcategoria)
        context={'juegos':juegos,'categorias':categorias}
        return render(request,'cliente/Juegos/game.html',context)
   


#carrito
@login_required
def carrito(request,correo):
    
    carrito=Carrito.objects.get(correo_cliente=correo)
    carritos=Carrito.objects.all()
    context={'carrito':carrito}
    return render(request, 'cliente/Juegos/carrito.html', context)



def carrito_add(request,correo,idjuego):
        carrito=Carrito.objects.get(correo_cliente=correo)
        juegos=Juegos.objects.get(idjuego = idjuego)
        
        carrito.juegos.add(juegos)
        carrito.actualizar_precio_total()
        carrito.save()    
        mensaje = 'Juego añadido al carrito'
        messages.success(request,mensaje)
        
        return redirect(request.META.get('HTTP_REFERER', 'cliente/Juegos/game.html'))
   
def carrito_del(request,correo,idjuego):
 
    carrito=Carrito.objects.get(correo_cliente=correo)
    juegos=Juegos.objects.get(idjuego = idjuego)
    carrito.juegos.remove(juegos)
    carrito.actualizar_precio_total()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))
        





from django.shortcuts import get_object_or_404, redirect, render
from .models import Carrito, Juegos

