# Generated by Django 4.2.4 on 2023-10-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0009_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='comentario',
            field=models.CharField(max_length=500, null=True),
        ),
    ]