from django.shortcuts import render, redirect
from .forms import ProfesorForm, AlumnoForm
from django.http import HttpResponse, HttpResponse
from .models import Catedra, Profesor, Alumno
from .forms import CatedraFormulario

# Create your views here.

def catedra(req, nombre, camada):
    
    catedra = Catedra(nombre=nombre, camada=camada)
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


def catedra_formulario(req) :
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        
        miFormulario = CatedraFormulario(req.POST)
        
        if miFormulario.is_valid():
            
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data
            
            catedra = Catedra(nombre=data["catedra"], camada=data["camada"])
            catedra.save()
            return render(req, "inicio.html", {"mensaje": "Catedra Asignada con exito"} )
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario Invalido"} )
    else:      
        
        miFormulario = CatedraFormulario()
        
        return render(req, "catedra_Formulario.html", {"miFormulario": miFormulario})
    
    
def busqueda_camada(req):
    
    return render(req, "busqueda_camada.html")

def buscar(req):
    
    if req.GET["camada"]:
        camada = req.GET["camada"]
        catedra = Catedra.objects.get(camada=camada)
        return render(req, "busqueda.html", {"catedra": catedra})
    else:
        return HttpResponse('Tu Busqueda No Coincide...')
    
    
def registrar_profesor(req):
    if req.method == 'POST':
        miFormulario = ProfesorForm(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data["nombre_profesor"], apellido=data["apellido_profesor"])
            profesor.save()
            return render(req, "inicio.html", {"mensaje": "Profesor Asignado con exito"} )
    else:
        miFormulario = ProfesorForm()
    return render(req, "registro_profesor.html", {"miFormulario": miFormulario})



def registrar_alumno(req):
    if req.method == 'POST':
        miFormulario = AlumnoForm(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            alumnos = Alumno(nombre=data["nombre_alumno"], apellido=data["apellido_alumno"])
            alumnos.save()
            return render(req, "inicio.html", {"mensaje": "Alumno Asignado con exito"} )
    else:
        miFormulario = AlumnoForm()
    return render(req, "registro_Alumno.html", {"miFormulario": miFormulario})






    




 
    


    