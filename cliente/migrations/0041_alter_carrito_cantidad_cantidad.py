# Generated by Django 4.1.2 on 2024-07-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0040_alter_carrito_cantidad_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito_cantidad',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]