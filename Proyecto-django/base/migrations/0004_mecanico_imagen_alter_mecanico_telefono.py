# Generated by Django 4.1.2 on 2024-06-11 23:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_mecanico_fecha_ingreso_alter_mecanico_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecanico',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mecanicos'),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='telefono',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]