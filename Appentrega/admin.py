from django.contrib import admin
from .models import Catedra, alumno, profesor, tareas

# Register your models here.

admin.site.register(Catedra)
admin.site.register(alumno)
admin.site.register(profesor)
admin.site.register(tareas)
