# Generated by Django 4.2.4 on 2023-10-07 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0005_alter_cocina_options_alter_pasteleria_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cocina',
            options={'verbose_name': 'Cocina', 'verbose_name_plural': 'Cocina'},
        ),
        migrations.AlterModelOptions(
            name='pasteleria',
            options={'verbose_name': 'Pastelería', 'verbose_name_plural': 'Pastelería'},
        ),
        migrations.AlterModelOptions(
            name='promociones',
            options={'verbose_name': 'Promoción', 'verbose_name_plural': 'Promociones'},
        ),
    ]
