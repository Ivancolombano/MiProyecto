"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppProyecto.views import pasteleria, cocina, promociones, lista_pasteleria, lista_cocina, lista_promociones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregapasteleria/<nombre>/<descripcion>/<precio>', pasteleria),
    path('agregacocina/<nombre>/<descripcion>/<precio>', cocina),
    path('agregapromociones/<nombre>/<descripcion>/<precio>', promociones),
    path('listadopasteleria/', lista_pasteleria),
    path('listadococina/', lista_cocina),
    path('listadopromociones/', lista_promociones),
]
