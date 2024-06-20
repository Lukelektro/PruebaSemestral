from django.shortcuts import render, get_object_or_404,redirect
#imports de login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
#Imports de mensajes
from django.contrib import messages
from datetime import datetime
#Imports de modelos y formularios
from .models import mecanico,Servicio
from .forms import mecanicoForm,contactoForm,servicioForm, citaForm, CustomUserCreationForm



#***************** definiciones de funciones basicas *****************

def soy_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

#***************** Autentificacion *****************

def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['username']
            contraseña = formulario.cleaned_data['password']
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                auth_login(request, usuario)
                messages.success(request, '¡Inicio de sesión exitoso!')
                return redirect('index')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'login.html', {'form': formulario})

#***************** Registro *****************

def registro(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)  # Autenticar al usuario después del registro
            return redirect('index')
    else:
        formulario = CustomUserCreationForm()

    return render(request, 'base/registro.html', {'form': formulario})

#***************** Vistas *****************
def index(request):
    
    #Codigo restante
    mecanicos = mecanico.objects.all()
    context = {
        "mecanicos":mecanicos,
        "soy_admin" :soy_admin(request.user) if request.user.is_authenticated else False
    }
    return render(request, 'base/index.html', context)



def trabajadores(request):
    #Codigo restante
    mecanicos = mecanico.objects.all()
    context = {
        "mecanicos":mecanicos,
        "soy_admin" :soy_admin(request.user) if request.user.is_authenticated else False
    }
    return render(request, 'base/trabajadores.html',context)

def servicios(request):
    
    #Codigo restante
    servicios = Servicio.objects.all()
    context = {
        "servicios":servicios,
        "soy_admin" :soy_admin(request.user) if request.user.is_authenticated else False
    }
    return render(request, 'base/servicios.html',context)

def nosotros(request):
    context = {
        "soy_admin" :soy_admin(request.user) if request.user.is_authenticated else False
    }
    #Codigo restante
    return render(request, 'base/nosotros.html', context)

def login(request):
    return render(request, 'base/login.html')

def logout(request):
    return render(request, 'base/logout.html')

def admin_cosas(request):
    #Codigo restante
    return render(request, 'base/admin_cosas.html')


#***************** CRUD Mecanico *****************

@login_required
def mecanico_list(request):
    mecanicos = mecanico.objects.all()
    context = {
        "mecanicos":mecanicos,
        "soy_admin" :soy_admin(request.user)
    }
    return render(request, 'base/mecanico_list.html', context)

@login_required
def mecanico_delete(request, id_mecanico):
    mecanico_to_delete = get_object_or_404(mecanico, id_mecanico=id_mecanico)
    mecanico_to_delete.delete()

    messages.success(request, 'Mecanico eliminado correctamente')
    return redirect('mecanico_list')

@login_required
def mecanico_add(request, id_mecanico=None):

    #Agarra la instancia del mecanico si existe id _mecanico
    instance = get_object_or_404(mecanico, id_mecanico=id_mecanico) if id_mecanico else None

    #Si el metodo es POST, se guarda el formulario
    if request.method == 'POST':

        #Si existe id_mecanico, se instancia el formulario con la instancia del mecanico
        form = mecanicoForm(request.POST,request.FILES ,instance=instance)

        #Si el formulario es valido, se guarda el mecanico
        if form.is_valid():

            form.save(commit=False)  
            form.fecha_ingreso = datetime.now()
            form.save()

            # Determinar si se está agregando o actualizando
            if id_mecanico:
                mensaje = 'Mecanico actualizado correctamente'
            else:
                form = mecanicoForm()
                mensaje = 'Mecanico agregado correctamente'
            
            
            #Se retorna el mensaje de que el mecanico fue guardado correctamente
            context = {
                'mensaje':mensaje,
                'form': form,
                'soy_admin' :soy_admin(request.user)
            }
            return render(request, 'base/mecanico_add.html', context)
        else:
        
            #Si el formulario no es valido, se retorna el formulario con los errores
            form = mecanicoForm(instance=instance)
            return render(request, 'base/mecanico_add.html', {'form': form})
            
    else:
        #Si el metodo no es POST, se instancia el formulario con la instancia del mecanico
        form = mecanicoForm(instance=instance)
        return render(request, 'base/mecanico_add.html', {'form': form})
    

    
#***************** CONTACTO *****************



def contacto(request):
    form_submitted = False  # Indicador de que el formulario se ha enviado correctamente

    if request.method == 'POST':

        form = contactoForm(request.POST)

        if form.is_valid():

            form.save()
            form_submitted = True  # Actualiza el indicador

            form = contactoForm()
        return render(request, 'base/contacto.html', {'form': form, 'form_submitted': form_submitted})

    else:
        form = contactoForm()
    
    context = {
        "soy_admin" :soy_admin(request.user) if request.user.is_authenticated else False,
        "form":form,
        "form_submitted": form_submitted
    }
    return render(request, 'base/contacto.html', context)



#***************** SERVICIOS *****************

@login_required
def servicio_list(request):
    servicios = Servicio.objects.all()
    context = {
        "servicios":servicios,
        "soy_admin" :soy_admin(request.user)
    }
    return render(request, 'base/servicio_list.html', context)

@login_required
def servicio_delete(request, id_servicio):
    servicio_to_delete = get_object_or_404(Servicio, id_servicio=id_servicio)
    servicio_to_delete.delete()

    messages.success(request, 'Servicio eliminado correctamente')
    return redirect('servicio_list')

@login_required
def servicio_add(request,id_servicio=None):

    instance = get_object_or_404(Servicio, id_servicio=id_servicio) if id_servicio else None

    if request.method == 'POST':

        form = servicioForm(request.POST,request.FILES,instance=instance)

        if form.is_valid():

            form.save()

            if id_servicio:
                mensaje = 'Servicio actualizado correctamente'
            else:
                form = servicioForm()
                mensaje = 'Servicio agregado correctamente'


            context = {
                'mensaje':mensaje,
                'form': form,
                'soy_admin' :soy_admin(request.user)
            }

            return render(request, 'base/servicio_add.html', context)
        else:
            form = servicioForm(instance=instance)
            return render(request, 'base/servicio_add.html', {'form': form})

    else:
        form = servicioForm(instance=instance)
        return render(request, 'base/servicio_add.html', {'form': form})
    
def servicio_detail(request,id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)

    form = citaForm();

    if request.method == 'POST':

        form = citaForm(request.POST)

        if form.is_valid():

            cita = form.save(commit=False)
            cita.servicio = servicio
            cita.save()
            
            form = citaForm()
            
        return render(request, 'base/servicio_detail.html', context)
        


    context = {'servicio':servicio,'form':form}
    return render(request, 'base/servicio_detail.html', context)

    