from django.shortcuts import render
from django.contrib.auth.models import User
from cliente.models import  Cliente,Juegos,Carrito,Carrousel_2025
from cliente.forms import ClienteForm,Juegos_Form,UserForm,CarruselForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import Http404
from django import template
# templatetags/custom_filters.py





# Create your views here.
def admin(request):
    context={}
    return render(request, 'administrador/admin.html', context)

def crud(request):
    clientes=Cliente.objects.all()
    context={'clientes':clientes}
    return render(request, 'administrador/crud.html', context)

#crud clientes

def clientes_del(request,pk):
    context={}
    cliente=Cliente.objects.get(email=pk)
    carrito=Carrito.objects.get(correo_cliente=pk)
    cliente.delete()
    carrito.delete()
    
    user=cliente.user
    user.delete()
    
    clientes=Cliente.objects.all()
    context={'clientes': clientes,}

    return redirect(request.META.get('HTTP_REFERER', '/'))

   


def clientes_edit(request,pk):
        #obtenemos los ruts de los clientes
        cliente=Cliente.objects.get(rut=pk)
       
        context={}
            #evaluamos si es post
        if request.method =="POST":
               
                form=ClienteForm(request.POST,instance=cliente)
                if form.is_valid() :
                    form.save()
                    
                    mensaje='DATOS ACTUALIZADOS'
                    messages.success(request,mensaje)
                    context = {'cliente': cliente, 'form': form,  'mensaje': mensaje}
                    return render(request,'administrador/cliente_edit.html',context)  
                else:
                    print("error")
                    context = {'cliente': cliente, 'form': form, 'form_errors': form.errors, 'formuser_errors': formuser.errors}
                    print(context)
                    return render(request,'administrador/cliente_edit.html',context)  
        else:
                 form=ClienteForm(instance=cliente)
                 context={'cliente':cliente,'form':form}
                 return render(request,'administrador/cliente_edit.html',context)


#crus juegos general
def crud_juegos(request):
    juegos=Juegos.objects.all()
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(juegos,5)
        juegos=paginator.page(page)
    except:
        raise Http404
    context={'entity':juegos,'paginator':paginator}
    return render(request, 'administrador/crud_juegos.html', context)



def juegos_add(request):
    context={}
    if request.method == "POST": 
        form=Juegos_Form(request.POST,request.FILES)
        print("es post")
        if form.is_valid():
            print("valido")
            form.save()
            form=Juegos_Form()
            mensaje="datos guardados"
            messages.success(request,mensaje)
            context={'mensaje':mensaje,'form':form}
            return render(request,'administrador/juegos_add.html',context)  
    else:
        
        form=Juegos_Form()
        context={'form':form}
        return render(request,'administrador/juegos_add.html',context)

def juegos_del(request,pk):
    context={}
    
    try:
        juegos=Juegos.objects.get(idjuego=pk)
        if juegos:
            juegos.delete()

            mensaje="datos eliminados"
            messages.success(request,mensaje)
            context={'juegos': juegos, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos.html',context)
        
    except:
        mensaje="rut no encontrado"
        juegos=Juegos.objects.all()
        context={'juegos': juegos, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos.html',context)


def juegos_edit(request,pk):
   
        #obtenemos los ids de los juegos de pc
        juegos=Juegos.objects.get(idjuego = pk)
        context={'form' : Juegos_Form(instance=juegos)}
         #evaluamos si es post
        if request.method == 'POST': 
                print("es un post")
                formulario=Juegos_Form(request.POST,request.FILES, instance=juegos)
                if formulario.is_valid():
                    formulario.save()
                    print("datos actualizados")
                    mensaje='DATOS ACTUALIZADOS'
                    messages.success(request,mensaje)
                    context={'mensaje':mensaje}
                return redirect('juegos_edit', pk=pk)

        return render(request,'administrador/juegos_edit.html',context)



def crud_carrito(request):
    carrito=Carrito.objects.all()
    context={'carrito':carrito}
    return render(request, 'administrador/crud_carrito.html', context)

def crud_carrusel(request):
    carrusel=Carrousel_2025.objects.all()
    context={'carrusel':carrusel}
    return render(request, 'administrador/crud_carrusel.html', context)

def carrusel_add(request):
    context={}
    if request.method == "POST": 
        nombre = request.POST.get('nombre', '')
        existe=Carrousel_2025.objects.filter(nombre=nombre).exists()
        if existe:
            messages.error(request,"El nombre se encuentra registrado")
            return render(request, 'administrador/carrusel_add.html')

        form=CarruselForm(request.POST,request.FILES)
        print("es post")
        if form.is_valid():
            print("valido")
            form.save()
            form=CarruselForm()
            mensaje="Datos guardados"
            messages.success(request,mensaje)
            context={'mensaje':mensaje,'form':form}
            return render(request,'administrador/carrusel_add.html',context)  
    else:
        
        form=CarruselForm()
        context={'form':form}
        return render(request,'administrador/carrusel_add.html',context)

def carrusel_del(request,nombre):
    
    try:
        carrusel=Carrousel_2025.objects.get(nombre=nombre)
        carrusel.delete()
        mensaje="Datos Eliminados"
        messages.success(request,mensaje)
        context={'carrusel': carrusel, 'mensaje':mensaje}
        return render(request,'administrador/crud_carrusel.html',context)
        
    except:
        mensaje="no encontrado"
        carrusel=Carrousel_2025.objects.all()
        context={'carrusel': carrusel, 'mensaje':mensaje}
        return render(request,'administrador/crud_carrusel.html',context)
    
def carrusel_edit(request,nombre):
   
        #obtenemos los ids de los juegos de pc
        carrusel=Carrousel_2025.objects.get(nombre = nombre)
        context={'form' : CarruselForm(instance=carrusel)}
         #evaluamos si es post
        if request.method == 'POST': 
                print("es un post")
                formulario=CarruselForm(request.POST,request.FILES, instance=carrusel)
                if formulario.is_valid():
                    formulario.save()
                    print("datos actualizados")
                    mensaje='DATOS ACTUALIZADOS'
                    messages.success(request,mensaje)
                    context={'mensaje':mensaje}
                return redirect('carrusel_edit', nombre=nombre)

        return render(request,'administrador/carrusel_edit.html',context)