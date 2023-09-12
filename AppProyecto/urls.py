from django.urls import path
from .views import *

urlpatterns = [
    path('agregapasteleria/<nombre>/<descripcion>/<precio>', pasteleria),
    path('agregacocina/<nombre>/<descripcion>/<precio>', cocina),
    path('agregapromociones/<nombre>/<descripcion>/<precio>', promociones),
    path('listapasteleria/', lista_pasteleria),
    path('listacocina/', lista_cocina),
    path('listapromociones/', lista_promociones),
    path('', inicio, name="Inicio"),
    path('pasteleria/', pasteleria, name="Pastelería"),
    path('cocina/', cocina, name="Cocina"),
    path('promociones/', promociones, name="Promociones"),
    path('iniciar-sesion/', inicio_de_sesion, name="Iniciar sesión"),
]