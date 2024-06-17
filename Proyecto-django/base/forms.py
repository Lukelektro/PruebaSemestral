from django import forms
from .models import mecanico,MensajeContacto,Servicio
from django.core.validators import MaxValueValidator

class mecanicoForm(forms.ModelForm):
    nombre = forms.CharField(required=True,max_length=50)
    apellido = forms.CharField(required=True,max_length=50)
    telefono = forms.IntegerField(required=True,validators=[MaxValueValidator(9999999999)]) 
    correo = forms.EmailField(required=True,max_length=50)
    sucursal = forms.ChoiceField(required=True,choices=[('vinadelmar','Viña del Mar'),('quilpue','Quilpue ')]) 
    especialidad = forms.CharField(required=True,max_length=50)
    experiencia = forms.CharField(max_length=50)
    descripcion = forms.CharField(required=True,widget=forms.Textarea)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = mecanico 
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'sucursal', 'especialidad','experiencia','descripcion','imagen']

#**************** FORM CONTACTO ****************
class contactoForm(forms.ModelForm):
    email = forms.EmailField(required=True,max_length=50)
    telefono = forms.IntegerField(required=True)
    direccion = forms.CharField(required=True,max_length=50)
    sucursal = forms.ChoiceField(required=True,choices=[('vinadelmar','Viña del Mar'),('quilpue','Quilpue ')])
    mensaje = forms.CharField(required=True,widget=forms.Textarea)

    class Meta:
        model = MensajeContacto
        fields = ['email', 'telefono', 'direccion', 'sucursal', 'mensaje']
        
#**************** FORM SERVICIO ****************

class servicioForm(forms.ModelForm):
    nombre = forms.CharField(required=True,max_length=50)
    descripcion = forms.CharField(required=True,widget=forms.Textarea)
    precio = forms.DecimalField(required=True,max_digits=10, decimal_places=2)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'imagen']