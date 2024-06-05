from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.servicio, name='servicio'),
    path('employes/', views.trabajadores, name='trabajadores'),
]