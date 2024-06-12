from django import forms
from .models import mecanico
<<<<<<< HEAD
from django.core.validators import MaxValueValidator, MinValueValidator

class mecanicoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.IntegerField(validators=[MaxValueValidator(9999999999)]) 
    correo = forms.EmailField(max_length=50)
    direccion = forms.CharField(max_length=50)
    especialidad = forms.CharField(max_length=50)

    class Meta:
        model = mecanico 
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'direccion', 'especialidad','imagen']

=======

from django.forms import ModelForm


class mecanicoForm(ModelForm):
    class Meta:
        model = mecanico 
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'direccion', 'especialidad']
>>>>>>> 6fab12373ed2ff4fb03d74f63cba00f28d2ceec4
