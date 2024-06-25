# Generated by Django 4.1.2 on 2024-06-24 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0016_delete_juegos_pc_delete_juegos_ps4_delete_juegos_ps5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puntuacion_juegos',
            fields=[
                ('idcategoria', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='juegos',
            name='puntuacion',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]