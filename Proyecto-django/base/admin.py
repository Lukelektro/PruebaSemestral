from django.contrib import admin
from .models import mecanico, MensajeContacto, Servicio,Cita
# Register your models here.
admin.site.register(mecanico)
admin.site.register(MensajeContacto)
admin.site.register(Servicio)
admin.site.register(Cita)
