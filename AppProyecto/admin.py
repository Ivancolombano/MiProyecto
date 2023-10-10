from django.contrib import admin
from .models import Pasteleria, Cocina, Promociones, Avatar

# Register your models here.
admin.site.register(Pasteleria)
admin.site.register(Cocina)
admin.site.register(Promociones)
admin.site.register(Avatar)