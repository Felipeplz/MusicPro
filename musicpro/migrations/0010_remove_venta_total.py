# Generated by Django 3.2.4 on 2021-07-03 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicpro', '0009_auto_20210703_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total',
        ),
    ]
