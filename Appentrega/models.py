from django.db import models

# Create your models here.

class Catedra(models.Model):
    nombre=models.CharField(max_length=30)
    camada=models.IntegerField()
    def __str__(self):
        return self.nombre
    
    
    
class Alumno(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(null=True)
    def __str__(self):
        return self.nombre
    
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    profesion=models.CharField(max_length=30)
    email=models.EmailField(null=True)  
    catedra = models.ManyToManyField(Catedra)
    
    

    
    
