# Generated by Django 4.1.2 on 2024-06-30 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0036_juegos_cantidad_jugadores_juegos_mas18_juegos_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='precio_total',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
    ]