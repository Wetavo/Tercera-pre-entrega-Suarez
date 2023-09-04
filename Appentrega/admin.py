from django.contrib import admin
from .models import Catedra, alumno, Profesor

# Register your models here.

admin.site.register(Catedra)
admin.site.register(alumno)
admin.site.register(Profesor)

