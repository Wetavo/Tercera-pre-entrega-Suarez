from django import forms

class CatedraFormulario(forms.Form) :
    
    catedra=forms.CharField(required=True)
    camada=forms.IntegerField(required=True)
    
