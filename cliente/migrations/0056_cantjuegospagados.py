# Generated by Django 4.1.13 on 2024-07-19 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0055_alter_juegospagados_correo_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CantJuegosPagados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.juegos')),
                ('juegos_pagados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.juegospagados')),
            ],
        ),
    ]
