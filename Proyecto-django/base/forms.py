from django import forms
from .models import mecanico
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

