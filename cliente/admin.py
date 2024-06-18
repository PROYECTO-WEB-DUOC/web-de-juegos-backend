from django.contrib import admin
from .models import Genero, Cliente, Juegos_Pc,Juegos_Ps5
# Register your models here.
##importamos para que aparezca en admin
admin.site.register(Genero)
admin.site.register(Cliente)
admin.site.register(Juegos_Pc)
admin.site.register(Juegos_Ps5)
