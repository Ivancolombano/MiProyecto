from django.http import HttpResponse
from django.shortcuts import render
from .models import Pasteleria, Cocina, Promociones

# Create your views here.

#Funciones pasteleria

def pasteleria(req, nombre, descripcion, precio):

    pasteleria = Pasteleria(nombre=nombre, descripcion=descripcion, precio=precio)
    pasteleria.save()

    return HttpResponse(f"""
    <p>Pastelería: {pasteleria.nombre} {pasteleria.descripcion} - Precio: $ {pasteleria.precio} agregado con éxito!</p>""")


def lista_pasteleria(req):

    lista = Pasteleria.objects.all()

    return render(req, "lista_pasteleria.html", {"lista_pasteleria": lista})



#Funciones cocina


def cocina(req, nombre, descripcion, precio):

    cocina = Cocina(nombre=nombre,descripcion=descripcion, precio=precio)
    cocina.save()

    return HttpResponse(f"""
    <p>Cocina: {cocina.nombre} {cocina.descripcion} - Precio: $ {cocina.precio} agregado con éxito!</p>""")


def lista_cocina(req):

    lista = Cocina.objects.all()

    return render(req, "lista_cocina.html", {"lista_cocina": lista})


#Funciones promociones


def promociones(req, nombre, descripcion, precio):

    promociones = Promociones(nombre=nombre, descripcion=descripcion, precio=precio)
    promociones.save()

    return HttpResponse(f"""
    <p>Promociones: {promociones.nombre} {promociones.descripcion} - Precio: $ {promociones.precio} agregado con éxito!</p>""")


def lista_promociones(req):

    lista = Promociones.objects.all()

    return render(req, "lista_promociones.html", {"lista_promociones": lista})


