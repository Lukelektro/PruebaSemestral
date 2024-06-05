# Create your views here.
from django.shortcuts import render

# Create your views here.

def login(request):
    context= {}
    return render(request, 'usuario\Login.html', context)