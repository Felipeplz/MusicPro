# Generated by Django 3.2.4 on 2021-07-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicpro', '0010_remove_venta_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
