from django.shortcuts import render, redirect
from inicio.models import Camiseta
from inicio.forms import CrearCamisetaForm

def inicio(request):
    return render(request, "inicio/inicio.html", {})


def camisetas(request):
    
    listado_de_camisetas = Camiseta.objects.all()
    
    return render(request, "inicio/camisetas.html", {"listado_de_camisetas" : listado_de_camisetas})

def crear_camiseta(request):
    
    # print(request.GET)
    # print("---------")
    # return render(request, "inicio/crear_camiseta.html" ,{})
    
    if request.method == "POST":
        formulario = CrearCamisetaForm(request.POST)
        
        if formulario.is_valid():
            info_limplia = formulario.cleaned_data
        
            marca = info_limplia.get("marca")
            descripcion = info_limplia.get("descripcion")
            equipo = info_limplia.get("equipo")
            anio = info_limplia.get("anio")
            
            camiseta = Camiseta(marca=marca, equipo=equipo, descripcion=descripcion, anio=anio)
            camiseta.save()  
            
            return redirect("camisetas")
        else:
            return render(request, "inicio/crear_camiseta.html", {"formulario":formulario})    
        
    formulario = CrearCamisetaForm()    
    return render(request, "inicio/crear_camiseta.html", {"formulario":formulario})
    
    
