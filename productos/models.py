from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(TimeStampedModel):
    
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    