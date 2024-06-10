from django.shortcuts import render
from .models import mecanico

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
