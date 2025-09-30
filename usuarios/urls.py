# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('', views.inicio, name='inicio'),
    path('perfil/', views.perfil, name='perfil'), 
    path('modulos/',views.modulos, name= 'modulos'),
    path('modulos/', views.modulos, name='modulos'),
    path('modulo1/', views.modulo1, name='modulo1'),
    path('prueba-mod1/', views.pruebaMod1, name='pruebaMod1'),
]