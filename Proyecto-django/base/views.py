from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
#imports de login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
#Imports de mensajes
from django.contrib import messages
from datetime import datetime
#Imports de modelos y formularios
from .models import mecanico,Servicio,clienteUser,Cita,Carrito
from .forms import mecanicoForm,contactoForm,servicioForm, citaForm, usuarioNuevosParametros, CarritoForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST


#***************** definiciones de funciones basicas *****************

def soy_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

def is_superuser(user):
    return user.is_superuser


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

@csrf_protect
def registro(request):
    if request.method == 'POST':
        formulario = usuarioNuevosParametros(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            auth_login(request, usuario)  # Autenticar al usuario después del registro
            return redirect('index')
    else:
        formulario = usuarioNuevosParametros()

    return render(request, 'base/registro.html', {'form': formulario})

#***************** Vistas *****************
def index(request):
    
    #Codigo restante
    mecanicos = mecanico.objects.all()
    servicios = Servicio.objects.all()

    context = {
        "servicios":servicios,
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
    
    servicios = Servicio.objects.all()
    context = {
        "servicios": servicios,  
        'esta_autentificado': request.user.is_authenticated,
        "soy_admin": soy_admin(request.user) if request.user.is_authenticated else False
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

#***************** CRUD Mecanico *****************

@login_required
@user_passes_test(is_superuser)
def mecanico_list(request):
    mecanicos = mecanico.objects.all()
    context = {
        "mecanicos":mecanicos,
        "soy_admin" :soy_admin(request.user)
    }
    return render(request, 'base/mecanico_list.html', context)

@login_required
@user_passes_test(is_superuser)
def mecanico_delete(request, id_mecanico):
    mecanico_to_delete = get_object_or_404(mecanico, id_mecanico=id_mecanico)
    mecanico_to_delete.delete()

    messages.success(request, 'Mecanico eliminado correctamente')
    return redirect('mecanico_list')

@login_required
@user_passes_test(is_superuser)
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

            context = {
                "soy_admin" :soy_admin(request.user) if request.user.is_authenticated else False,
                "form":form,
                "form_submitted": form_submitted
            }
        return render(request, 'base/contacto.html', context)

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
@user_passes_test(is_superuser)
def servicio_list(request):
    servicios = Servicio.objects.all()
    context = {
        "servicios":servicios,
        "soy_admin" :soy_admin(request.user)
    }
    return render(request, 'base/servicio_list.html', context)

@login_required
@user_passes_test(is_superuser)
def servicio_delete(request, id_servicio):
    servicio_to_delete = get_object_or_404(Servicio, id_servicio=id_servicio)
    servicio_to_delete.delete()

    messages.success(request, 'Servicio eliminado correctamente')
    return redirect('servicio_list')

@login_required
@user_passes_test(is_superuser)
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



@login_required
def servicio_detail(request,id_servicio):

    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    usuario, created = clienteUser.objects.get_or_create(user=request.user)
    

    form = citaForm();

    if request.method == 'POST':

        form = citaForm(request.POST)

        if form.is_valid():

            cita = form.save(commit=False)
            cita.usuario = usuario.user
            cita.servicio = servicio
            cita.save()
            
            form = citaForm()
            context = {'servicio':servicio,'form':form,'mensaje':'Cita agendada correctamente'}
            return render(request, 'base/servicio_detail.html', context)
        
        return render(request, 'base/servicio_detail.html', {'servicio':servicio,'form':form})
    
    context = {'servicio':servicio,'form':form}
    return render(request, 'base/servicio_detail.html', context)

#***************** CITAS *****************

@login_required
def citas(request):

    citas = Cita.objects.filter(usuario=request.user)  

    context = {
        "citas": citas,
        "soy_admin": soy_admin(request.user) 
    }
    return render(request, 'base/citas.html', context)

@login_required
@user_passes_test(is_superuser)
def citas_admin(request):

    citas = Cita.objects.filter()  

    context = {
        "citas": citas,
        "soy_admin": soy_admin(request.user) 
    }
    return render(request, 'base/citas_admin.html', context)

#***************** Carrito *****************

def carrito(request):
    return render(request, 'base/carrito.html')

@require_POST
def agregar_al_carrito(request):
    usuario_id = request.user.id
    servicio_id = request.POST.get('servicio_id')
    patente = request.POST.get('patente')
    servicio = Servicio.objects.get(id_servicio=servicio_id)
    usuario = User.objects.get(id=usuario_id)

    carrito, created = Carrito.objects.get_or_create(
        usuario=usuario,
        servicio=servicio,
        patente=patente,
        defaults={'cantidad': 1, 'precio_en_el_momento': servicio.precio}
    )

    if not created:
        carrito.cantidad += 1
        carrito.save()

    return JsonResponse({'success': True, 'mensaje': 'Servicio agregado al carrito correctamente'})
