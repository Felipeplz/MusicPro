# Generated by Django 3.2.4 on 2021-07-03 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicpro', '0006_delete_promocion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='idSucursalRetiro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicpro.sucursal'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='mail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
