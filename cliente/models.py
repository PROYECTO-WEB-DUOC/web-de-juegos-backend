from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    contraseña=models.CharField(max_length=10, null=False)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
    

class Genero(models.Model):
    idgenero = models.CharField(primary_key=True,max_length=10)
    genero = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)