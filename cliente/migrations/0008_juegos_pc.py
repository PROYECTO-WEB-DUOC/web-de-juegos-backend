# Generated by Django 4.1.2 on 2024-06-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_alter_cliente_contraseña'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juegos_Pc',
            fields=[
                ('idjuego', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('puntuacion', models.CharField(max_length=2)),
                ('precio', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]
