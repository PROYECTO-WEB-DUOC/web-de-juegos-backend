from django.shortcuts import render
from .models import  Cliente,Genero,Juegos,Categoria_juegos,Carrousel_2025,Carrito,CantJuegos
from .forms import ClienteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
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

def carrito(request):
    correo = request.user.email
    carrito = get_object_or_404(Carrito, correo_cliente=correo)
    context = {'carrito': carrito}
    return render(request, 'cliente/Juegos/carrito.html', context)




def carrito_add(request, correo, idjuego):
    carrito = Carrito.objects.get(correo_cliente=correo)
    juego =Juegos.objects.get( idjuego=idjuego)
    cant_juego, created = CantJuegos.objects.get_or_create(carrito=carrito, juego=juego)
    if not created:
        cant_juego.cantidad += 1
        cant_juego.save()
    carrito.actualizar_precio_total()
    carrito.save()
    
    mensaje = 'Juego añadido al carrito'
    messages.success(request, mensaje)
    
    return redirect(request.META.get('HTTP_REFERER', 'cliente/Juegos/game.html'))


def carrito_del(request, correo, idjuego):
    carrito = Carrito.objects.get(correo_cliente=correo)
    juego =Juegos.objects.get( idjuego=idjuego)
    cant_juego = CantJuegos.objects.get(carrito=carrito, juego=juego)

    if cant_juego.cantidad > 1:
        cant_juego.cantidad -= 1
        cant_juego.save()
    else: 
        cant_juego.delete()
    
    
    carrito.actualizar_precio_total()
    carrito.save()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

        






