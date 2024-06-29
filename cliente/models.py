from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Cliente(models.Model):
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
    id_categoria = models.ForeignKey('Categoria_juegos',on_delete=models.CASCADE, db_column='idcategoria')
    video=models.FileField(upload_to="cliente", null=False)
    estreno=models.BooleanField(default= False)
    def __str__(self):
        return str(self.nombre)

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
    juegos  =models.ManyToManyField('Juegos' ,null=True)
    precio_total = models.CharField(max_length=20 ,null=True)

    def actualizar_precio_total(self):
        total = sum(float(juego.precio) for juego in self.juegos.all())
        self.precio_total = str(total)
        self.save()

    def __str__(self):
        return str(self.idcarrito)