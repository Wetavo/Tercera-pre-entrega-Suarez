from django.urls import path
from Appentrega.views import catedra, lista_catedra, inicio, alumnos, profesores, tareas


urlpatterns = [
    
    path('agrega-catedra/<nombre>/<camada>', catedra),
    path('lista-catedra/', lista_catedra),
    path('', inicio),
    path('catedra/', catedra),
    path('profesores/', profesores),
    path('alumnos/', alumnos),
    path('tareas/', tareas),  
    
    ]  