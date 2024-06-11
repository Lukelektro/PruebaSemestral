from django.shortcuts import render
from datetime import datetime
from .models import mecanico
from .forms import mecanicoForm

# Create your views here.
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

def mecanico_list(request):
    mecanicos = mecanico.objects.all()
    context={"mecanicos":mecanicos}
    return render(request, 'base/mecanico_list.html', context)



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