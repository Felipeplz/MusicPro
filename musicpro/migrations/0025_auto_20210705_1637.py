# Generated by Django 3.2.4 on 2021-07-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicpro', '0024_auto_20210705_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Percusión', 'Percusión'), ('Amplificadores', 'Amplificadores'), ('Accesorios varios', 'Accesorios varios'), ('Instrumentos de Cuerdas', 'Instrumentos de Cuerdas')], max_length=50),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]