from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class mecanico(models.Model):
    id_mecanico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    experiencia = models.CharField(max_length=50)
    fecha_ingreso = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='mecanicos', null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
    #Sobreescribir el metodo delete para borrar la imagen del mecanico
    def delete(self, *args, **kwargs):
        self.imagen.delete(save=False)
        super().delete(*args, **kwargs)
    



