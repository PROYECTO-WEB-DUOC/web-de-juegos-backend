from django.shortcuts import render
from .models import  Cliente,Genero
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context={}
    return render(request, 'cliente/index.html', context)

def crud(request):
    clientes=Cliente.objects.all()
    context={'clientes': clientes}
    return render(request, 'cliente/crud.html', context)

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
        return render(request,'cliente/Registros/crearc.html', context)
def registro(request):
    context={}
    return render(request, 'cliente/Registros/registro.html', context)

def clientes_del(request,pk):
    context={}
    try:
        cliente=Cliente.objects.get(rut=pk)
        cliente.delete()

        mensaje="datos eliminados"
        clientes=Cliente.objects.all()
        context={'clientes': clientes, 'mensaje':mensaje}
        return render(request,'cliente/crud.html',context)

    except:
        mensaje="rut no encontrado"
        clientes=Cliente.objects.all()
        context={'clientes': clientes, 'mensaje':mensaje}
        return render(request,'cliente/crud.html',context)


def clientes_edit(request,pk):
    try:
        #obtenemos los ruts de los clientes
        cliente=Cliente.objects.get(rut=pk)
        context={}
        if cliente:
            #evaluamos si es post
            if request.method =="POST":
                form=ClienteForm(request.POST,instance=cliente)
                form.save()
                mensaje='DATOS ACTUALIZADOS'
                
                context={'cliente':cliente,'form':form,'mensaje':mensaje}
                return render(request,'cliente/crud.html',context)
            else:
                #no es un post
                 
                 form=ClienteForm(instance=cliente)
                 context={'cliente':cliente,'form':form}
                 return render(request,'cliente/crud.html',context)
    except:
        print("rut no existe")
        clientes=Cliente.objects.all()
        
        context={'clientes':clientes}
        return render(request,'cliente/crud.html',context)


def index(request):
    request.session["usuario"]="maxi"
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render(request, 'cliente/index.html', context)