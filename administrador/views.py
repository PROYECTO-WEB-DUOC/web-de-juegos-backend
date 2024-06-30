from django.shortcuts import render
from django.contrib.auth.models import User
from cliente.models import  Cliente,Juegos
from cliente.forms import ClienteForm,Juegos_Form,UserForm
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
    cliente=Cliente.objects.get(rut=pk)
    cliente.delete()
    
    user=cliente.user
    user.delete()
    
    clientes=Cliente.objects.all()
    context={'clientes': clientes, 'mensaje':mensaje}
    return render(request,'administrador/crud.html',context)

   


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
                    context = {'cliente': cliente, 'form': form,  'mensaje': mensaje}
                    return render(request,'administrador/crud.html',context)  
                else:
                    print("error")
                    context = {'cliente': cliente, 'form': form, 'form_errors': form.errors, 'formuser_errors': formuser.errors}
                    print(context)
                    return render(request,'administrador/crud.html',context)  
        else:
                 form=ClienteForm(instance=cliente)
                 context={'cliente':cliente,'form':form}
                 return render(request,'administrador/crud.html',context)


#crus juegos general
def crud_juegos(request):
    juegos=Juegos.objects.all()
    context={'juegos':juegos}
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
            context={'mensaje':mensaje,'form':form}
            return render(request,'administrador/crud_juegos.html',context)  
    else:
        print("error")
        form=Juegos_Form()
        context={'form':form}
        return render(request,'administrador/crud_juegos.html',context)

def juegos_del(request,pk):
    context={}
    
    try:
        juegos=Juegos.objects.get(idjuego=pk)
        if juegos:
            juegos.delete()

            mensaje="datos eliminados"
            
            context={'juegos': juegos, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos.html',context)
        
    except:
        mensaje="rut no encontrado"
        juegos=Juegos.objects.all()
        context={'juegos': juegos, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos.html',context)


def juegos_edit(request,pk):
    try:
        #obtenemos los ids de los juegos de pc
        juegos=Juegos.objects.get(idjuego = pk)
        context={'form' : Juegos_Form(instance=juegos)}
        if juegos:
            print("encontro")
            #evaluamos si es post
            if request.method == 'POST': 
                print("es un post")
                formulario=Juegos_Form(request.POST,request.FILES, instance=juegos)
                if formulario.is_valid:
                    formulario.save()
                    print("datos actualizados")
                    mensaje='DATOS ACTUALIZADOS'
                    
                    context={'mensaje':mensaje}
            

        return render(request,'administrador/juegos_edit.html',context)
    except:
        mensaje="id no encontrado"
        juegos=Juegos.objects.all()
        context={'juegos':juegos, 'mensaje':mensaje}
        return render(request,'administrador/juegos_edit.html',context)