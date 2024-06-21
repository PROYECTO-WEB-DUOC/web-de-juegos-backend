from django.contrib import admin
from .models import Genero, Cliente,Juegos,Categoria_juegos
# Register your models here.
##importamos para que aparezca en admin
admin.site.register(Genero)
admin.site.register(Cliente)

admin.site.register(Juegos)
admin.site.register(Categoria_juegos)