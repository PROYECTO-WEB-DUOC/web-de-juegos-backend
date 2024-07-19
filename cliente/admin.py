from django.contrib import admin
from .models import Genero, Cliente,Juegos,Categoria_juegos,Carrousel_2025,Carrito,CantJuegos,JuegosPagados
# Register your models here.
##importamos para que aparezca en admin
admin.site.register(Genero)
admin.site.register(Cliente)

admin.site.register(Juegos)
admin.site.register(Categoria_juegos)
admin.site.register(Carrousel_2025)
admin.site.register(Carrito)
admin.site.register(CantJuegos)
admin.site.register(JuegosPagados)