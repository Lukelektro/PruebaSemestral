from django.contrib import admin
from .models import mecanico, MensajeContacto, Servicio, Cliente,Carrito

# Register your models here.
admin.site.register(mecanico)
admin.site.register(MensajeContacto)
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Carrito)
