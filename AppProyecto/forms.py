from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar, Usuario

class Pasteleriaformulario(forms.Form):

    pasteleria = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=500)
    precio = forms.DecimalField(max_digits=10, decimal_places=0)
    


class Cocinaformulario(forms.Form):    

    cocina = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=500)
    precio = forms.DecimalField(max_digits=10, decimal_places=0)
    

class Promocionesformulario(forms.Form):

    promociones = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=500)
    precio = forms.DecimalField(max_digits=10, decimal_places=0)


class UsuarioFormulario(forms.ModelForm):

    class Meta:
        model=Usuario
        fields = ("nombre", "apellido", "email")




class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text= "",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)



    class Meta:
        model=User
        fields = ["email", "first_name", "last_name", "password1", "password2"]
        
    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
           raise forms.ValidationError("Las contraseñan no coinciden!")
        return password2


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ("imagen",)




class PedidoPasteleriaFormulario(forms.Form):

    cantidad = forms.DecimalField(max_digits=10, decimal_places=0)
    comentario = forms.CharField(max_length=500, required=False)
    

    def __str__(self):
        return f'{self.comentario}  ${self.cantidad}'
    
    class Meta:
        verbose_name = "Pedidos"
        verbose_name_plural = "Pedidos"


class PedidoCocinaFormulario(forms.Form):

    cantidad = forms.DecimalField(max_digits=10, decimal_places=0)
    comentario = forms.CharField(max_length=500, required=False)
    

    def __str__(self):
        return f'{self.comentario}  ${self.cantidad}'
    
    class Meta:
        verbose_name = "Pedidos"
        verbose_name_plural = "Pedidos"
    

class PedidoPromocionesFormulario(forms.Form):

    cantidad = forms.DecimalField(max_digits=10, decimal_places=0)
    comentario = forms.CharField(max_length=500, required=False)
    

    def __str__(self):
        return f'{self.comentario}  ${self.cantidad}'
    
    class Meta:
        verbose_name = "Pedidos"
        verbose_name_plural = "Pedidos"