from django.contrib import admin
from .models import Catedra, Alumno, Profesor

# Register your models here.

admin.site.register(Catedra)
admin.site.register(Alumno)
admin.site.register(Profesor)

