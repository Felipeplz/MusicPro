# Generated by Django 3.2.4 on 2021-07-03 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('foto', models.CharField(max_length=250)),
                ('marca', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('subtipo', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=200, unique=True)),
                ('rut', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12, null=True)),
                ('direccion', models.CharField(max_length=250, null=True)),
                ('rol', models.CharField(choices=[('Cliente', 'Cliente'), ('Vendedor', 'Vendedor'), ('Contador', 'Contador'), ('Bodeguero', 'Bodeguero'), ('Admin', 'Admin')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('total', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('mail', models.CharField(max_length=100)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicpro.usuario')),
                ('idSucursalRetiro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicpro.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDesde', models.DateField()),
                ('fechaHasta', models.DateField()),
                ('cantidadMin', models.IntegerField()),
                ('descuento', models.FloatField()),
                ('idProducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicpro.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPago', models.CharField(max_length=30)),
                ('montoTotal', models.IntegerField()),
                ('tipoDoc', models.CharField(max_length=30)),
                ('docTributario', models.CharField(max_length=100, null=True)),
                ('idVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicpro.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordenDespacho', models.CharField(max_length=100)),
                ('fechaEntrega', models.DateTimeField(auto_now_add=True)),
                ('idReceptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicpro.usuario')),
                ('idVenta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='musicpro.venta')),
            ],
        ),
        migrations.CreateModel(
            name='ItemVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('descuento', models.IntegerField(null=True)),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicpro.producto')),
                ('idVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicpro.venta')),
            ],
            options={
                'unique_together': {('idVenta', 'idProducto')},
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEstado', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('En Carrito', 'En Carrito'), ('Pagado', 'Pagado'), ('En Camino', 'En Camino'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado')], max_length=30)),
                ('comentario', models.CharField(max_length=250, null=True)),
                ('documento', models.CharField(max_length=250, null=True)),
                ('idVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicpro.venta')),
            ],
            options={
                'unique_together': {('idVenta', 'fechaEstado')},
            },
        ),
    ]