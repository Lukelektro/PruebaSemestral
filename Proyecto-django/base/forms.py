from django import forms
from django.core.validators import MaxValueValidator
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
from .models import mecanico,MensajeContacto,Servicio,Cita, clienteUser

#**************** FORM REGISTRO/USUARIO ****************

class usuarioNuevosParametros(UserCreationForm):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    correo = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    telefono = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=50)

    class Meta:
        model = User 
        fields = ('username', 'nombre', 'apellido', 'correo', 'telefono', 'ciudad', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['correo']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            profile = clienteUser.objects.create(
                user=user,
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                correo=self.cleaned_data['correo'],
                telefono=self.cleaned_data['telefono'],
                ciudad=self.cleaned_data['ciudad']
            )
        return user



#**************** FORM MECANICO ****************
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
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'imagen']


    
#**************** FORM CITA ****************
HORAS_DISPONIBLES = [
    ('09:00', '09:00 AM'),
    ('11:00', '11:00 AM'),
    ('13:00', '01:00 PM'),
    ('15:00', '03:00 PM'),
]
class citaForm(forms.ModelForm):
    
    fecha = forms.DateField(required=True,initial=datetime.date.today,widget=NumberInput(attrs={'type': 'date'}))
    hora = forms.ChoiceField(required=True,choices=HORAS_DISPONIBLES,widget=forms.Select())
    marca = forms.CharField(required=True,max_length=50)
    patente = forms.CharField(required=True,max_length=50)
    comentario = forms.CharField(required=True,widget=forms.Textarea)
    

    class Meta:
        model = Cita
        fields = ['fecha', 'hora', 'marca', 'patente', 'comentario']
