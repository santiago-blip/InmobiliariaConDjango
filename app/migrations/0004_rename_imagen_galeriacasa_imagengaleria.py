# Generated by Django 3.2.8 on 2021-10-07 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_casa_galeriacasa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galeriacasa',
            old_name='imagen',
            new_name='imagenGaleria',
        ),
    ]