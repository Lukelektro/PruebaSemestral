# Generated by Django 5.0.6 on 2024-06-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_mensajecontacto_remove_mecanico_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecanico',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
