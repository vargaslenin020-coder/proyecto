# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('', views.inicio, name='inicio'),
    path('perfil/', views.perfil, name='perfil'), # Nueva URL para el perfil
    path('modulos/',views.modulos, name= 'modulos'),
]