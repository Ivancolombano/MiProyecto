from django.db import models

# Create your models here.

class Pasteleria(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=0, help_text='$')


class Cocina(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=0, help_text='$') 

class Promociones(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=0, help_text='$')      
