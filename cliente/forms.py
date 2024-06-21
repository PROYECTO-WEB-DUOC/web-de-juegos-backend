from django import forms
from django.forms import ModelForm
from .models import Cliente,Juegos

class ClienteForm(ModelForm):

    class Meta:
        model= Cliente
        fields=[ 'rut',
                'nombre',
                'apellido_paterno',
                'id_genero', 
                'email',
                'contraseña',] 



class Juegos_Form(ModelForm):

    class Meta:
        model= Juegos
        fields='__all__'