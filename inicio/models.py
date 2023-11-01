from django.db import models

class Camiseta(models.Model):
    marca = models.CharField(max_length=30)
    equipo = models.TextField() 
    descripcion = models.TextField() 
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.equipo} - {self.descripcion} - {self.anio}"

class Pantalon(models.Model):
    marca = models.CharField(max_length=30)
    equipo = models.TextField() 
    descripcion = models.TextField() 
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.equipo} - {self.descripcion} - {self.anio}"
    
class Medias(models.Model):
    marca = models.CharField(max_length=30)
    equipo = models.TextField() 
    descripcion = models.TextField() 
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.equipo} - {self.descripcion} - {self.anio}"    

