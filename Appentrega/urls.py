from django.urls import path
from Appentrega.views import *




urlpatterns = [
    
    path('agregar-catedra/<nombre>/<camada>', catedra, name="Agregar"),
    path('lista-catedra/', lista_catedra),
    path('', inicio, name="Inicio"),
    path('catedra/', catedra, name="Catedra"),
    path('profesores/', profesores,),
    path('alumnos/', alumnos,),
    
    path('catedra-formulario/', catedra_formulario, name="CatedraFormulario"), #Para Agregar Alguna Catedra
    path('busqueda_camada/', busqueda_camada, name="busquedacamada"), #Para Buscar Alguna Camada
    path('buscar/', buscar, name="Buscar"),
    path('registrar-profesor/', registrar_profesor, name="RegistrarProfesor"), 
    path('registrar-alumno/', registrar_alumno, name="RegistrarAlumno"),
    
    
]  