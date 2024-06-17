# Generated by Django 5.0.6 on 2024-06-17 17:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_mecanico_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('correo', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='servicios')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.cliente')),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.servicio')),
            ],
        ),
    ]