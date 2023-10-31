from django import forms

class CrearCamisetaForm(forms.Form):
    marca = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    anio = forms.IntegerField()
    
    
