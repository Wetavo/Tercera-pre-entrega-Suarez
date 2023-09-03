from django.db import models

# Create your models here.

class Catedra(models.Model):
    nombre=models.CharField(max_length=30)
    camada=models.IntegerField()
    
class alumno(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(null=True)
    
class profesor(models.Model):
    nnombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    profesion=models.CharField(max_length=30)
    email=models.EmailField(null=True)  
    
class tareas(models.Model):
    asignatura=models.CharField(max_length=30)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()  
