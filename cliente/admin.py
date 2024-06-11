from django.contrib import admin
from .models import Genero, Cliente
# Register your models here.
##importamos para que aparezca en admin
admin.site.register(Genero)
admin.site.register(Cliente)
