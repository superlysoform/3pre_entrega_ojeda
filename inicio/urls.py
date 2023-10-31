from django.urls import path
from inicio.views import inicio, camisetas, crear_camiseta
 

urlpatterns = [
    path("", inicio,name="inicio"),
    path("camisetas/", camisetas, name="camisetas"),
    path("camisetas/crear/", crear_camiseta, name="crear_camiseta"),
    
]