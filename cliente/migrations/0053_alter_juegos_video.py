# Generated by Django 4.1.13 on 2024-07-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0052_alter_juegos_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegos',
            name='video',
            field=models.TextField(blank=True, null=True),
        ),
    ]
