
# Create your views here.
from django.shortcuts import render

# Create your views here.

def contacto(request):
    context= {}
    return render(request, 'contacto/Contacto.html', context)

def nosotros(request):
    context= {}
    return render(request, 'contacto/nosotros.html', context)