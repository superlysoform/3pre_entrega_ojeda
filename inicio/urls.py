from django.urls import path
from inicio.views import inicio, camisetas, pantalones, medias, crear_camiseta, crear_pantalon, crear_medias
 

urlpatterns = [
    path("", inicio,name="inicio"),
    path("camisetas/", camisetas, name="camisetas"),
    path("pantalones/", pantalones, name="pantalones"),
    path("medias/", medias, name="medias"),
    
    path("camisetas/crear/", crear_camiseta, name="crear_camiseta"),
    path("pantalones/crear/", crear_pantalon, name="crear_pantalon"),
    path("medias/crear/", crear_medias, name="crear_medias"),

    
]