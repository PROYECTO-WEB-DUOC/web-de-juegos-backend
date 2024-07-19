from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    contraseña=models.CharField(max_length=10, null=False)
    carrito=models.ForeignKey('Carrito',on_delete=models.CASCADE, db_column='idcarrito',null=True)
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
    

class Genero(models.Model):
    idgenero = models.CharField(primary_key=True,max_length=10)
    genero = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)




class Juegos(models.Model):
    idjuego=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    puntuacion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    precio=models.CharField(max_length=20)
    imagen=models.ImageField( upload_to="cliente", null=False)
    cantidad_jugadores=models.CharField(max_length=100)
    online=models.BooleanField(default=False)
    mas18=models.BooleanField(default=False)
    id_categoria = models.ForeignKey('Categoria_juegos',on_delete=models.CASCADE, db_column='idcategoria')
    video=models.TextField(null=True, blank=True) 
    estreno=models.BooleanField(default= False)
    stock =models.IntegerField( null=True)
    def __str__(self):
        return str(self.nombre)

    def del_stock(self):
        if self.stock > 0:
            self.stock -= 1
            self.save()
       
        self.save()
    def add_stock(self):
        self.stock += 1
        self.save()


    def cantidad_en_carrito(self):
        return sum(juego.cantidad for juego in self.cantjuegos_set.all())

class Categoria_juegos(models.Model):
    idcategoria = models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)

class Carrousel_2025 (models.Model):
    nombre=models.CharField(max_length=100)
    imagen=models.ImageField( upload_to="cliente", null=False)

    def __str__(self):
        return str(self.nombre)


class Carrito(models.Model):
    idcarrito=models.AutoField(primary_key=True)
    correo_cliente=models.EmailField(unique=True, max_length=100, blank=True, null=False)
    juegos = models.ManyToManyField(Juegos, through='CantJuegos')
    precio_total = models.CharField(max_length=20 ,null=True,default=0)
    
    def actualizar_precio_total(self):
        total = sum(float(item.juego.precio) * item.cantidad for item in self.cantjuegos_set.all())
        self.precio_total = str(total)
        self.save()
    
    def total_juegos(self):
        return sum(item.cantidad for item in self.cantjuegos_set.all())

    def __str__(self):
        return str(self.idcarrito)
    

class CantJuegos(models.Model):
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    juego = models.ForeignKey('Juegos', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    

class JuegosPagados(models.Model):
    idpeticion=models.AutoField(primary_key=True)
    correo_cliente=models.EmailField(unique=False, max_length=100, blank=True, null=False)
    juegos = models.ManyToManyField(Juegos)
    precio_total = models.CharField(max_length=20 ,null=True,default=0)

class CantJuegosPagados(models.Model):
    juegos_pagados = models.ForeignKey(JuegosPagados, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juegos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)   