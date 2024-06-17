from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime
from .models import mecanico,Servicio
from .forms import mecanicoForm,contactoForm,servicioForm


# Create your views here.


#***************** Vistas *****************
def index(request):
    mecanicos = mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'base/index.html', context)



def trabajadores(request):
    mecanicos = mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'base/trabajadores.html',context)

def servicios(request):
    return render(request, 'base/servicios.html')

def nosotros(request):
    return render(request, 'base/nosotros.html')

def login(request):
    return render(request, 'base/login.html')


#***************** CRUD Mecanico *****************

def mecanico_list(request):
    mecanicos = mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'base/mecanico_list.html', context)

def mecanico_delete(request, id_mecanico):
    mecanico_to_delete = get_object_or_404(mecanico, id_mecanico=id_mecanico)
    mecanico_to_delete.delete()

    messages.success(request, 'Mecanico eliminado correctamente')
    return redirect('mecanico_list')

def mecanico_add(request, id_mecanico=None):

    #Agarra la instancia del mecanico si existe id _mecanico
    instance = get_object_or_404(mecanico, id_mecanico=id_mecanico) if id_mecanico else None

    #Si el metodo es POST, se guarda el formulario
    if request.method == 'POST':

        #Si existe id_mecanico, se instancia el formulario con la instancia del mecanico
        form = mecanicoForm(request.POST,request.FILES ,instance=instance)

        #Si el formulario es valido, se guarda el mecanico
        if form.is_valid():
            mecanico_instance = form.save(commit=False)  
            mecanico_instance.fecha_ingreso = datetime.now()
            mecanico_instance.save()

            # Determinar si se está agregando o actualizando
            if id_mecanico:
                mensaje = 'Mecanico actualizado correctamente'
            else:
                mensaje = 'Mecanico agregado correctamente'
            
            form = mecanicoForm(instance=mecanico_instance)
            
            #Se retorna el mensaje de que el mecanico fue guardado correctamente
            context = {'mensaje':mensaje,'form': form}
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
    
    return render(request, 'base/contacto.html', {'form': form, 'form_submitted': form_submitted})

#***************** SERVICIOS *****************

def servicio_list(request):
    servicios = Servicio.objects.all()
    context={"servicios":servicios}
    return render(request, 'base/servicio_list.html', context)

def servicio_delete(request, id_servicio):
    servicio_to_delete = get_object_or_404(Servicio, id_servicio=id_servicio)
    servicio_to_delete.delete()

    messages.success(request, 'Servicio eliminado correctamente')
    return render(request, 'base/servicio_list.html')

def servicio_add(request):

    if request.method == 'POST':

        form = servicioForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            form = servicioForm()
        return render(request, 'base/servicio_add.html', {'form': form})

    else:
        form = servicioForm()
        return render(request, 'base/servicio_add.html', {'form': form})