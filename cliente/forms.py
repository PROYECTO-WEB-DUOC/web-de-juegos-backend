from django import forms
from django.forms import ModelForm
from .models import Cliente,Juegos
from django.contrib.auth.models import User
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido_paterno', 'id_genero', 'email', 'contraseña', 'carrito'] 



class Juegos_Form(ModelForm):

    class Meta:
        model= Juegos
        fields='__all__'




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']



