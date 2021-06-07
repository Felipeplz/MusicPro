from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, DateTimeCheckMixin, DateTimeField, IntegerField

# Create your models here.
class SQLDespachos(models.Model):
    id_venta = models.IntegerField()
    orden_despacho = models.CharField(max_length=30)
    fecha_entrega = models.DateTimeField()
    id_receptor = models.IntegerField()
    mail = models.CharField(max_length=100)

    class Meta:
        unique_together = (("id_venta", "orden_despacho"))
        managed = False
        db_table = 'DESPACHO'

class SQLEstadoPedidos(models.Model):
    id_venta = models.IntegerField()
    fecha_estado = models.DateTimeField()
    estado = models.CharField(max_length=30)
    comentario = models.CharField(max_length=50)
    documento = models.CharField(max_length=250)

    class Meta:
        unique_together = (("id_venta", "fecha_estado"))
        managed = False
        db_table = 'ESTADO_PEDIDO'

class SQLItemVentas(models.Model):
    id_venta = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        unique_together = (("id_venta", "id_producto"))
        managed = False
        db_table = 'ITEM_VENTA'

class SQLPagos(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    tipo_pago = models.CharField(max_length=30)
    monto_total = models.IntegerField()
    tipo_doc = models.CharField(max_length=30)
    doc_tributario = models.CharField(max_length=50)
    id_venta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PEGO'

class SQLProductos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
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
    
    class Meta:
        managed = False
        db_table = 'PRODUCTO'

    def __str__(self): 
      return self.nombre

class SQLPromociones(models.Model):
    id_promocion = models.IntegerField(primary_key=True)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    cantidad_min = models.IntegerField()
    descuento = models.FloatField()
    id_producto = models.IntegerField()

class SQLSucursales(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'SUCURSAL'

class SQLUsuarios(models.Model):
    ROLES = (
        ('Cliente','Cliente'),
        ('Vendedor','Vendedor'),
        ('Contador','Contador'),
        ('Bodeguero','Bodeguero'),
        ('Admin','Admin'),
    )

    id_usuario = models.IntegerField(primary_key=True)
    mail = models.CharField(max_length=100)
    contrasennia = models.CharField(max_length=50)
    rut = models.IntegerField()
    dv_rut = models.CharField(max_length=1, help_text="Dígito verificador")
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    rol = models.CharField(max_length=30, choices=ROLES)

    class Meta:
        managed = False
        db_table = 'USUARIO'

class SQLVentas(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    total = models.IntegerField()
    descuento = models.IntegerField()
    id_cliente = models.IntegerField()
    id_sucursal_retiro = models.IntegerField()
    mail = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'VENTA'