from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class SQLProductos(models.Model):
    id_producto = models.IntegerField()
    codigo_producto = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    foto = models.CharField(max_length=250)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=50)
    subtipo = models.CharField(max_length=40)
    categoria = models.CharField(max_length=50)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=500)