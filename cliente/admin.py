from django.contrib import admin
from .models import  Cliente
# Register your models here.
##importamos para que aparezca en admin

admin.site.register(Cliente)
