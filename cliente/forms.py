from django import forms
from django.forms import ModelForm
from .models import Cliente

class ClienteForm(ModelForm):

    class Meta:
        model= Cliente
        fields=[ 'rut',
                'nombre',
                'apellido_paterno',
                'id_genero', 
                'email',
                'contraseña',] 


