from django.shortcuts import render, redirect
from inicio.models import Camiseta, Pantalon, Medias
from inicio.forms import CrearCamisetaForm, CrearPantalonForm, CrearMediasForm, BusquedaCamisetaForm, BusquedaPantalonForm, BusquedaMediasForm

def inicio(request):
    return render(request, "inicio/inicio.html", {})


def camisetas(request):
    
    formulario = BusquedaCamisetaForm(request.GET)
    if formulario.is_valid():
        busqueda_marca = formulario.cleaned_data.get("marca")
        listado_de_camisetas = Camiseta.objects.filter(marca__icontains=busqueda_marca)
                 
    formulario = BusquedaCamisetaForm()
    return render(request, "inicio/camisetas.html", {"formulario": formulario, "listado_de_camisetas":listado_de_camisetas})

    
def pantalones(request):
        
    formulario = BusquedaPantalonForm(request.GET)
    if formulario.is_valid():
        busqueda_marca = formulario.cleaned_data.get("marca")
        listado_de_pantalones = Pantalon.objects.filter(marca__icontains=busqueda_marca)
                 
    formulario = BusquedaPantalonForm()
    return render(request, "inicio/pantalones.html", {"formulario": formulario, "listado_de_pantalones":listado_de_pantalones})

    # return render(request, "inicio/pantalones.html", {})

def medias(request):
    
    formulario = BusquedaMediasForm(request.GET)
    if formulario.is_valid():
        busqueda_marca = formulario.cleaned_data.get("marca")
        listado_de_medias = Medias.objects.filter(marca__icontains=busqueda_marca)
                 
    formulario = BusquedaMediasForm()
    return render(request, "inicio/medias.html", {"formulario": formulario, "listado_de_medias":listado_de_medias})


def crear_camiseta(request):
    
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
    
def crear_pantalon(request):
    
    if request.method == "POST":
        formulario = CrearPantalonForm(request.POST)
        
        if formulario.is_valid():
            info_limplia = formulario.cleaned_data
        
            marca = info_limplia.get("marca")
            descripcion = info_limplia.get("descripcion")
            equipo = info_limplia.get("equipo")
            anio = info_limplia.get("anio")
            
            pantalon = Pantalon(marca=marca, equipo=equipo, descripcion=descripcion, anio=anio)
            pantalon.save()  
            
            return redirect("pantalon")
        else:
            return render(request, "inicio/crear_pantalon.html", {"formulario":formulario})    
        
    formulario = CrearPantalonForm()    
    return render(request, "inicio/crear_pantalon.html", {"formulario":formulario})
    
def crear_medias(request):
    
    if request.method == "POST":
        formulario = CrearMediasForm(request.POST)
        
        if formulario.is_valid():
            info_limplia = formulario.cleaned_data
        
            marca = info_limplia.get("marca")
            descripcion = info_limplia.get("descripcion")
            equipo = info_limplia.get("equipo")
            anio = info_limplia.get("anio")
            
            medias = Medias(marca=marca, equipo=equipo, descripcion=descripcion, anio=anio)
            medias.save()  
            
            return redirect("medias")
        else:
            return render(request, "inicio/crear_medias.html", {"formulario":formulario})    
        
    formulario = CrearMediasForm()    
    return render(request, "inicio/crear_medias.html", {"formulario":formulario})    
    
    
    # busqueda_marca = request.GET.get("marca")
    # if busqueda_marca:
    #     listado_de_camisetas = Camiseta.objects.filter(marca_icontains=busqueda_marca)
    # else:
    #     listado_de_camisetas = Camiseta.objects.all()