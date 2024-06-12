<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from datetime import datetime
from .models import mecanico
from .forms import mecanicoForm


# Create your views here.


#***************** Vistas *****************
=======
from django.shortcuts import render
from datetime import datetime
from .models import mecanico
from .forms import mecanicoForm

# Create your views here.
>>>>>>> 6fab12373ed2ff4fb03d74f63cba00f28d2ceec4
def index(request):
    mecanicos = mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'base/index.html', context)

def Contacto(request):
    return render(request, 'base/Contacto.html')

def trabajadores(request):
    return render(request, 'base/trabajadores.html')

def servicios(request):
    return render(request, 'base/servicios.html')

def nosotros(request):
    return render(request, 'base/nosotros.html')

def login(request):
    return render(request, 'base/login.html')

<<<<<<< HEAD

#***************** CRUD Mecanico *****************

=======
>>>>>>> 6fab12373ed2ff4fb03d74f63cba00f28d2ceec4
def mecanico_list(request):
    mecanicos = mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'base/mecanico_list.html', context)

<<<<<<< HEAD
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
        form = mecanicoForm(request.POST, request.FILES, instance=instance)

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
    

    
=======


#***************** CRUD Mecanico *****************

def mecanico_add(request):
    form = mecanicoForm()
    context = {"form": form}
    return render(request, 'base/mecanico_add.html', context)


def crud_mecanico(request):
    mecanicos = mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'base/mecanico_list.html', context)

def mecanico_create(request):

    context = {}

    if request.method == 'POST':
        form = mecanicoForm(request.POST)
        if form.is_valid():
            mecanico = form.save(commit=False)
            mecanico.fecha_ingreso = datetime.now()
            form.save()

            form = mecanicoForm()
            context={'mensaje':'Guardado correctamente', 'form':form}

            return render(request, 'base/mecanico_add.html', context)
    else:
        form = mecanicoForm()
        context={'form':form}
        return render(request, 'base/mecanico_add.html', context)
>>>>>>> 6fab12373ed2ff4fb03d74f63cba00f28d2ceec4
