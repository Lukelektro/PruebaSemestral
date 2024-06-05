from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('contacto/', views.Contacto, name='contacto'),
    path('trabajadores/', views.trabajadores, name='trabajadores'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
]