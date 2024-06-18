from django import forms
from django.forms import ModelForm
from .models import Cliente, Juegos_Pc,Juegos_Ps5,Juegos_Ps4

class ClienteForm(ModelForm):

    class Meta:
        model= Cliente
        fields=[ 'rut',
                'nombre',
                'apellido_paterno',
                'id_genero', 
                'email',
                'contraseña',] 

class Juegos_Pc_Form(ModelForm):

    class Meta:
        model= Juegos_Pc
        fields='__all__'

class Juegos_Ps5_Form(ModelForm):

    class Meta:
        model= Juegos_Ps5
        fields='__all__'


class Juegos_Ps4_Form(ModelForm):

    class Meta:
        model= Juegos_Ps4
        fields='__all__'