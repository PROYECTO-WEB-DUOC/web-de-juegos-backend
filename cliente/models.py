from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
    

