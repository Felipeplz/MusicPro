from django.db.models.aggregates import Sum
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db.models.fields import CharField, DateField, DateTimeCheckMixin, DateTimeField, IntegerField
from django.db.models import Count, Q, Case, When, Exists

# Create your models here.
class Usuario(models.Model):
    ROLES = (
        ('Cliente','Cliente'),
        ('Vendedor','Vendedor'),
        ('Contador','Contador'),
        ('Bodeguero','Bodeguero'),
        ('Admin','Admin'),
    )

    mail = models.CharField(max_length=200, unique=True)
    rut = models.CharField(max_length=15)
    telefono = models.CharField(max_length=12, null=True, blank=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    rol = models.CharField(max_length=9, choices=ROLES)
    suscrito = models.BooleanField(default=False)

    def __str__(self): 
      return self.rol + " " + self.mail

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=12)

    def __str__(self): 
      return self.nombre

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)
    sucursalRetiro = models.ForeignKey('Sucursal', on_delete=models.CASCADE, null=True , blank=True)
    direccion = models.CharField(max_length=250, null=True , blank=True)
    comuna = models.CharField(max_length=100, null=True , blank=True)
    token = models.CharField(max_length=100)
    total = models.IntegerField(null=True, blank=True)
    
    def __str__(self): 
      return self.cliente.mail + " " + str(self.fecha)

class Despacho(models.Model):
    idVenta = models.OneToOneField('Venta', on_delete=models.CASCADE)
    ordenDespacho = models.CharField(max_length=100)
    fechaEntrega = models.DateTimeField(auto_now_add=True)
    receptor = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)

class Estado(models.Model):
    ESTADOS = (
        ('En Carrito','En Carrito'),
        ('Pago Pendiente','Pago Pendiente'),
        ('Pagado','Pagado'),
        ('En Camino','En Camino'),
        ('Enviado','Enviado'),
        ('Entregado','Entregado'),
    )

    venta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=False)
    fechaEstado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=30, choices=ESTADOS)
    comentario = models.CharField(max_length=250, null=True, blank=True)
    documento = models.CharField(max_length=250, null=True, blank=True)
    encargado = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self): 
      return self.estado + " " + str(self.venta)

    class Meta:
        unique_together = (("venta", "fechaEstado"))

class ItemVenta(models.Model):
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=False)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = (("venta", "producto"))

class Pago(models.Model):
    tipoPago = models.CharField(max_length=30)
    montoTotal = models.IntegerField()
    tipoDoc = models.CharField(max_length=30)
    docTributario = models.CharField(max_length=100, null=True)
    idVenta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=False)

class Producto(models.Model):
    CATEGORIAS = {
      ('Instrumentos de Cuerdas','Instrumentos de Cuerdas'),
      ('Percusión','Percusión'),
      ('Amplificadores','Amplificadores'),
      ('Accesorios varios','Accesorios varios'),
    }

    nombre = models.CharField(max_length=150)
    foto = models.FileField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=50)
    subtipo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=500, null=True)

    def __str__(self): 
      return self.nombre

    @property
    def precioPromo(self):
        return int(self.precio*0.9)

