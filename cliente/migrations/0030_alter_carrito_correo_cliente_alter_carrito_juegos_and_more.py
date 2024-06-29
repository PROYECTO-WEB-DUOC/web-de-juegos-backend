# Generated by Django 4.1.2 on 2024-06-29 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0029_remove_carrito_run_cliente_carrito_correo_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='correo_cliente',
            field=models.EmailField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='juegos',
            field=models.ManyToManyField(null=True, to='cliente.juegos'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='precio_total',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
