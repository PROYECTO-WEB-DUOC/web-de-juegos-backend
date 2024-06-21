from django.shortcuts import render
from django.contrib.auth.models import User
from cliente.models import  Cliente,Juegos_Pc,Juegos_Ps5,Juegos_Ps4
from cliente.forms import ClienteForm,Juegos_Pc_Form, Juegos_Ps5_Form,Juegos_Ps4_Form
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
    try:
        cliente=Cliente.objects.get(rut=pk)
        cliente.delete()

        mensaje="datos eliminados"
        clientes=Cliente.objects.all()
        context={'clientes': clientes, 'mensaje':mensaje}
        return render(request,'administrador/crud.html',context)

    except:
        mensaje="rut no encontrado"
        clientes=Cliente.objects.all()
        context={'clientes': clientes, 'mensaje':mensaje}
        return render(request,'administrador/crud.html',context)


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
                return render(request,'administrador/crud.html',context)
            else:
                #no es un post
                 
                 form=ClienteForm(instance=cliente)
                 context={'cliente':cliente,'form':form}
                 return render(request,'administrador/crud.html',context)
    except:
        print("rut no existe")
        clientes=Cliente.objects.all()
        
        context={'clientes':clientes}
        return render(request,'administrador/crud.html',context)


def crud_juegos_pc(request):
    juegos_pc=Juegos_Pc.objects.all()
    context={'juegos_pc':juegos_pc}
    return render(request, 'administrador/crud_juegos_pc.html', context)

#crud juegos_pc
def juegos_pc_add(request):
    context={}
    if request.method == "POST": 
        form=Juegos_Pc_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=Juegos_Pc_Form()
            mensaje="datos guardados"
            context={'mensaje':mensaje,'form':form}
            return render(request,'administrador/crud_juegos_pc.html',context)  
    else:
        
        form=Juegos_Pc_Form()
        context={'form':form}
        return render(request,'administrador/crud_juegos_pc.html',context)

def juegos_pc_del(request,pk):
    context={}
    
    try:
        juegos_pc=Juegos_Pc.objects.get(idjuego=pk)
        if juegos_pc:
            juegos_pc.delete()

            mensaje="datos eliminados"
            
            context={'juegos_pc': juegos_pc, 'mensaje':mensaje}
            return render(request,'administrador/crud_juegos_pc.html',context)
        
    except:
        mensaje="rut no encontrado"
        juegos_pc=Juegos_Pc.objects.all()
        context={'juegos_pc': juegos_pc, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos_pc.html',context)


def juegos_pc_edit(request,pk):
    try:
        #obtenemos los ids de los juegos de pc
        juegos_pc=Juegos_Pc.objects.get(idjuego = pk)
        context={'form' : Juegos_Pc_Form(instance=juegos_pc)}
        if juegos_pc:
            print("encontro")
            #evaluamos si es post
            if request.method == 'POST': 
                print("es un post")
                formulario=Juegos_Pc_Form(request.POST,request.FILES, instance=juegos_pc)
                if formulario.is_valid:
                    formulario.save()
                    print("datos actualizados")
                    mensaje='DATOS ACTUALIZADOS'
                    
                    context={'mensaje':mensaje}
            

        return render(request,'administrador/crud_juegos_pc.html',context)
    except:
        mensaje="id no encontrado"
        juegos_pc=Juegos_Pc.objects.all()
        context={'juegos_pc': juegos_pc, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos_pc.html',context)
        


#crud juegos_ps5
def crud_juegos_ps5(request):
    juegos_ps5=Juegos_Ps5.objects.all()
    context={'juegos_ps5':juegos_ps5}
    return render(request, 'administrador/crud_juegos_ps5.html', context)



def juegos_ps5_add(request):
    context={}
    if request.method == "POST": 
        form=Juegos_Ps5_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=Juegos_Ps5_Form()
            mensaje="datos guardados"
            context={'mensaje':mensaje,'form':form}
            return render(request,'administrador/crud_juegos_ps5.html',context)  
    else:
        
        form=Juegos_Ps5_Form()
        context={'form':form}
        return render(request,'administrador/crud_juegos_ps5.html',context)

def juegos_ps5_del(request,pk):
    context={}
    
    try:
        juegos_ps5=Juegos_Ps5.objects.get(idjuego=pk)
        if juegos_ps5:
            juegos_ps5.delete()

            mensaje="datos eliminados"
            
            context={'juegos_ps5': juegos_ps5, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos_ps5.html',context)
        
    except:
        mensaje="rut no encontrado"
        juegos_ps5=Juegos_Ps5.objects.all()
        context={'juegos_ps5': juegos_ps5, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos_ps5.html',context)


def juegos_ps5_edit(request,pk):
    try:
        #obtenemos los ids de los juegos de pc
        juegos_ps5=Juegos_Ps5.objects.get(idjuego = pk)
        context={'form' : Juegos_Ps5_Form(instance=juegos_ps5)}
        if juegos_ps5:
            print("encontro")
            #evaluamos si es post
            if request.method == 'POST': 
                print("es un post")
                formulario=Juegos_Ps5_Form(request.POST,request.FILES, instance=juegos_ps5)
                if formulario.is_valid:
                    formulario.save()
                    print("datos actualizados")
                    mensaje='DATOS ACTUALIZADOS'
                    
                    context={'mensaje':mensaje}
            

        return render(request,'administrador/crud_juegos_ps5.html',context)
    except:
        mensaje="id no encontrado"
        juegos_ps5=Juegos_Ps5.objects.all()
        context={'juegos_ps5':juegos_ps5, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos_ps5.html',context)

#crud juegos_ps4
def crud_juegos_ps4(request):
    juegos_ps4=Juegos_Ps4.objects.all()
    context={'juegos_ps4':juegos_ps4}
    return render(request, 'administrador/crud_juegos_ps4.html', context)



def juegos_ps4_add(request):
    context={}
    if request.method == "POST": 
        form=Juegos_Ps4_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=Juegos_Ps4_Form()
            mensaje="datos guardados"
            context={'mensaje':mensaje,'form':form}
            return render(request,'administrador/crud_juegos_ps4.html',context)  
    else:
        
        form=Juegos_Ps4_Form()
        context={'form':form}
        return render(request,'administrador/crud_juegos_ps4.html',context)

def juegos_ps4_del(request,pk):
    context={}
    
    try:
        juegos_ps4=Juegos_Ps4.objects.get(idjuego=pk)
        if juegos_ps4:
            juegos_ps4.delete()

            mensaje="datos eliminados"
            
            context={'juegos_ps4': juegos_ps4, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos_ps4.html',context)
        
    except:
        mensaje="rut no encontrado"
        juegos_ps4=Juegos_Ps4.objects.all()
        context={'juegos_ps4': juegos_ps4, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos_ps4.html',context)


def juegos_ps4_edit(request,pk):
    try:
        #obtenemos los ids de los juegos de pc
        juegos_ps4=Juegos_Ps4.objects.get(idjuego = pk)
        context={'form' : Juegos_Ps4_Form(instance=juegos_ps4)}
        if juegos_ps4:
            print("encontro")
            #evaluamos si es post
            if request.method == 'POST': 
                print("es un post")
                formulario=Juegos_Ps4_Form(request.POST,request.FILES, instance=juegos_ps4)
                if formulario.is_valid:
                    formulario.save()
                    print("datos actualizados")
                    mensaje='DATOS ACTUALIZADOS'
                    
                    context={'mensaje':mensaje}
            

        return render(request,'administrador/crud_juegos_ps4.html',context)
    except:
        mensaje="id no encontrado"
        juegos_ps4=Juegos_Ps4.objects.all()
        context={'juegos_ps4':juegos_ps4, 'mensaje':mensaje}
        return render(request,'administrador/crud_juegos_ps4.html',context)