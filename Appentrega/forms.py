from django import forms

class CatedraFormulario(forms.Form) :
    
    catedra=forms.CharField(required=True)
    camada=forms.IntegerField(required=True)
    
    
class ProfesorForm(forms.Form):
    nombre_profesor = forms.CharField(max_length=100, label='Nombre del Profesor')
    
    

   
    
