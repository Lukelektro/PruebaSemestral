from django.shortcuts import render

# Create your views here.

def base(request):
    context={}
    return render(request, 'base/base.html', context)

def Contacto(request):
    return render(request, 'base/Contacto.html')

def trabajadores(request):
    return render(request, 'base/trabajadores.html')
def servicios(request):
    return render(request, 'base/servicios.html')

def nosotros(request):
    return render(request, 'base/nosotros.html')