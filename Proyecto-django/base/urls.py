from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('trabajadores/', views.trabajadores, name='trabajadores'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
    path('mecanico_list', views.mecanico_list, name='mecanico_list'),
    path('mecanico_add/', views.mecanico_add, name='mecanico_add_no_id'),
    path('mecanico_add/<int:id_mecanico>/', views.mecanico_add, name='mecanico_add'),
    path('mecanico/delete/<int:id_mecanico>/', views.mecanico_delete, name='mecanico_delete'),
    path('servicio_list/', views.servicio_list, name='servicio_list'),
    path('servicio_add/', views.servicio_add, name='servicio_add_no_id'),
    path('servicio_add/<int:id_servicio>/', views.servicio_add, name='servicio_add'),
    path('servicio/delete/<int:id_servicio>/', views.servicio_delete, name='servicio_delete'),
    path('servicio_detail/<int:id_servicio>/',views.servicio_detail, name='servicio_detail')
    ]