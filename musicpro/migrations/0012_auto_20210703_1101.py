# Generated by Django 3.2.4 on 2021-07-03 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicpro', '0011_alter_venta_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='mail',
        ),
    ]