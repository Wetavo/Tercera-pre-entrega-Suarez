from django.shortcuts import render
from django.http import HttpResponse
from .models import Catedra

# Create your views here.

def catedra(req, nombre, camada):
    catedra=Catedra(nombre = nombre, camada = camada)
    catedra.save()

    return HttpResponse(f"""<p>Catedra: {catedra.nombre} - Camada: {catedra.camada} agregado! </p>""")

def lista_catedra(req):
    
    lista = Catedra.objects.all()
    
    return render(req, "lista_catedra.html", {"lista_catedra": lista})

def inicio(req):
    return render(req, "inicio.html")
    

def catedra(req):
    return render(req, "catedra.html")


def profesores(req):
    return render(req, "profesores.html")


def alumnos(req):
    return render(req, "alumnos.html")


def tareas(req):
    return render(req, "tareas.html")