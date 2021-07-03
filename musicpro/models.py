from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db.models.fields import CharField, DateField, DateTimeCheckMixin, DateTimeField, IntegerField

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
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12, null=True, blank=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    rol = models.CharField(max_length=9, choices=ROLES)
    suscrito = models.BooleanField(default=False)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=12)

class Venta(models.Model):
    fecha = models.DateTimeField()
    total = models.IntegerField()
    descuento = models.IntegerField()
    idCliente = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)
    idSucursalRetiro = models.ForeignKey('Sucursal', on_delete=models.CASCADE, null=True)
    mail = models.CharField(max_length=100)

class Despacho(models.Model):
    idVenta = models.OneToOneField('Venta', on_delete=models.CASCADE)
    ordenDespacho = models.CharField(max_length=100)
    fechaEntrega = models.DateTimeField(auto_now_add=True)
    idReceptor = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)

class Estado(models.Model):
    ESTADOS = (
        ('En Carrito','En Carrito'),
        ('Pagado','Pagado'),
        ('En Camino','En Camino'),
        ('Enviado','Enviado'),
        ('Entregado','Entregado'),
    )

    idVenta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=False)
    fechaEstado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=30, choices=ESTADOS)
    comentario = models.CharField(max_length=250, null=True)
    documento = models.CharField(max_length=250, null=True)

    class Meta:
        unique_together = (("idVenta", "fechaEstado"))

class ItemVenta(models.Model):
    idVenta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=False)
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField()
    descuento = models.IntegerField(null=True)

    class Meta:
        unique_together = (("idVenta", "idProducto"))

class Pago(models.Model):
    tipoPago = models.CharField(max_length=30)
    montoTotal = models.IntegerField()
    tipoDoc = models.CharField(max_length=30)
    docTributario = models.CharField(max_length=100, null=True)
    idVenta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=False)

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    foto = models.FileField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=50)
    subtipo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=500, null=True)

    def __str__(self): 
      return self.nombre

class Promocion(models.Model):
    fechaDesde = models.DateField()
    fechaHasta = models.DateField()
    cantidadMin = models.IntegerField()
    descuento = models.FloatField()
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=True)


