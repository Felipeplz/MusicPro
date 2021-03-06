# Generated by Django 3.2.4 on 2021-07-04 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicpro', '0014_venta_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='despacho',
            old_name='idReceptor',
            new_name='receptor',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='idVenta',
            new_name='venta',
        ),
        migrations.RenameField(
            model_name='itemventa',
            old_name='idProducto',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='itemventa',
            old_name='idVenta',
            new_name='venta',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='idCliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='idSucursalRetiro',
            new_name='sucursalRetiro',
        ),
        migrations.AlterUniqueTogether(
            name='estado',
            unique_together={('venta', 'fechaEstado')},
        ),
        migrations.AlterUniqueTogether(
            name='itemventa',
            unique_together={('venta', 'producto')},
        ),
    ]
