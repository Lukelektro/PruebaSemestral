from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


#*************** MECANICO ****************
class mecanico(models.Model):
    id_mecanico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    correo = models.CharField(max_length=50)
    sucursal = models.CharField(max_length=50,null=True, blank=True)
    especialidad = models.CharField(max_length=50)
    experiencia = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='mecanicos', null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
    #Sobreescribir el metodo delete para borrar la imagen del mecanico
    def delete(self, *args, **kwargs):
        self.imagen.delete(save=False)
        super().delete(*args, **kwargs)

#*************** MENSAJE CONTACTO ****************

class MensajeContacto(models.Model):
    id_name = models.AutoField(primary_key=True)
    email  = models.EmailField()
    telefono = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    direccion = models.CharField(max_length=50)
    sucursal = models.CharField(max_length=50)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)


#*************** SERVICIOS ****************

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(null=True,validators=[MaxValueValidator(9999999999)])
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='servicios', null=True, blank=True)

    def __str__(self):
        return self.nombre

    #Sobreescribir el metodo delete para borrar la imagen del servicio
    def delete(self, *args, **kwargs):
        self.imagen.delete(save=False)
        super().delete(*args, **kwargs)

#*************** LOGIN/USUARIO ****************


class clienteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)
    id_unico = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.username


    
#*************** CITA ****************

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='citas',null=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.CharField(max_length=50)
    marca = models.CharField(max_length=50,null=True)
    patente = models.CharField(max_length=50,null=True)
    comentario = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        usuario_info = "Unknown User"
        if self.usuario:
            cliente_user = self.usuario.clienteuser  # Assuming reverse relation is named 'clienteuser'
            usuario_info = f"{cliente_user.nombre} {cliente_user.apellido}"
        return f"{usuario_info} - {self.servicio.nombre} - {str(self.fecha)} - {str(self.hora)}"