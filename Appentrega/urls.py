from django.urls import path
from Appentrega.views import *


urlpatterns = [
    
    path('agregar-catedra/<nombre>/<camada>', catedra, name="Agregar"),
    path('lista-catedra/', lista_catedra),
    path('', inicio, name="Inicio"),
    path('catedra/', catedra, name="Catedra"),
    path('profesores/', profesores, name="Profesores"),
    path('alumnos/', alumnos, name="Alumnos"),
    path('tareas/', tareas, name="Tareas"),  
    path('catedra-formulario/', catedra_formulario, name="CatedraFormulario"), 
    path('busqueda_camada/', busqueda_camada, name="busquedacamada"), 
    path('buscar/', buscar, name="Buscar"), 
]  