from django.db import models

# Create your models here.


class mecanico(models.Model):
    id_mecanico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    experiencia = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    


