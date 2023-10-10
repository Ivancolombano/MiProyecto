from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pasteleria(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=0, help_text='$')
    creado = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.nombre}  ${self.precio}'
    
    class Meta:
        verbose_name = "Pastelería"
        verbose_name_plural = "Pastelería"
        



class Cocina(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=0, help_text='$')
    creado = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.nombre}  ${self.precio}'
    
    class Meta:
        verbose_name = "Cocina"
        verbose_name_plural = "Cocina"
        
    
   

class Promociones(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=0, help_text='$')
    creado = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.nombre}  ${self.precio}'
    

    class Meta:
        verbose_name = "Promoción"
        verbose_name_plural = "Promociones"


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='Avatares', blank=True, null=True)       
        



class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    user = models. OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    


class Pedido(models.Model):

    cantidad = models.DecimalField(max_digits=10, decimal_places=0)
    comentario = models.CharField(max_length=500, null=True)
    

    def __str__(self):
        return f'{self.comentario}  ${self.cantidad}'
    
    class Meta:
        verbose_name = "Pedidos"
        verbose_name_plural = "Pedidos"