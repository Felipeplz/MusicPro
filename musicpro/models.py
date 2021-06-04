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

class SQLDespachos(models.Model):
    id_venta = models.IntegerField()
    orden_despacho = models.CharField(max_length=30)
    fecha_entrega = models.DateTimeField()
    id_receptor = models.IntegerField()
    mail = models.CharField(max_length=100)

class SQLItemVentas(models.Model):
    id_venta = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()

class SQLPagos(models.Model):
    id_pago = models.IntegerField()
    tipo_pago = models.CharField(max_length=30)
    monto_total = models.IntegerField()
    tipo_doc = models.CharField(max_length=30)
    doc_tributario = models.CharField(max_length=50)
    id_venta = models.IntegerField()

class SQLPromocions(models.Model):
    id_promocion = models.IntegerField()
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    cantidad_min = models.IntegerField()
    id_producto = models.IntegerField()

class SQLRols(models.Model):
    id_rol = models.IntegerField()
    nombre_rol = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)

class SQLSucursals(models.Model):
    id_sucursal = models.IntegerField()
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

class SQLUsuarios(models.Model):
    id_usuario = models.IntegerField()
    mail = models.CharField(max_length=100)
    rut = models.IntegerField()
    dv_rut = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    id_rol = models.IntegerField()

class SQLVentas(models.Model):
    id_venta = models.IntegerField()
    fecha = models.DateTimeField()
    total = models.IntegerField()
    descuento = models.IntegerField()
    id_cliente = models.IntegerField()
    id_sucursal_retiro = models.IntegerField()
    mail = models.CharField(max_length=100)
