from django.db import models

class Camiseta(models.Model):
    marca = models.CharField(max_length=30)
    equipo = models.TextField() 
    descripcion = models.TextField() 
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.equipo} - {self.descripcion} - {self.anio}"

# class Producto(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     def _str_(self):
#         return self.nombre

# class Persona(models.Model):
#     nombre = models.CharField(max_length=100)
#     edad = models.IntegerField()
#     correo = models.EmailField()

#     def _str_(self):
#         return self.nombre


# class Tarea(models.Model):
#     titulo = models.CharField(max_length=200)
#     descripcion = models.TextField()
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     fecha_vencimiento = models.DateTimeField()
#     def _str_(self):
#         return self.titulo