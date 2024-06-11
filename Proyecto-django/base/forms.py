from django import forms
from .models import mecanico

from django.forms import ModelForm


class mecanicoForm(ModelForm):
    class Meta:
        model = mecanico 
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'direccion', 'especialidad']