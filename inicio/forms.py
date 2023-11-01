from django import forms

class CrearCamisetaForm(forms.Form):
    marca = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    anio = forms.IntegerField()
    

class CrearPantalonForm(forms.Form):
    marca = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    anio = forms.IntegerField()

class CrearMediasForm(forms.Form):
    marca = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    anio = forms.IntegerField()
    
    
class BusquedaCamisetaForm(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    
class BusquedaPantalonForm(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    
class BusquedaMediasForm(forms.Form):
    marca = forms.CharField(max_length=30, required=False)