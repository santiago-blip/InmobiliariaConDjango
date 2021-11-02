# Generated by Django 3.2.7 on 2021-10-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('numeroCelular', models.CharField(max_length=50, null=True)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='perfil/')),
                ('admin_access', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'tbl_usuario',
            },
        ),
    ]