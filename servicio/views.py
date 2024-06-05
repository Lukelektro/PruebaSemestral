from django.shortcuts import render

# Create your views here.
def servicio(request):
    context = {}
    return render(request, 'servicio/servicios.html', context)

def trabajadores(request):
    context = {}
    return render(request, 'servicio/trabajadores.html', context)