# autos/admin.py

from django.contrib import admin
from .models import (
    Marca, TipoAuto, Modelo, TipoCombustible, Transmision, Color,
    Concesionario, Cliente, Vendedor, Auto, Venta, Servicio,
    AutoServicio, Seguro, AutoSeguro, Garantia, AutoGarantia,
    RegistroMantenimiento, Reparacion, AutoReparacion
)

# Registra cada modelo en el admin
admin.site.register(Marca)
admin.site.register(TipoAuto)
admin.site.register(Modelo)
admin.site.register(TipoCombustible)
admin.site.register(Transmision)
admin.site.register(Color)
admin.site.register(Concesionario)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Auto)
admin.site.register(Venta)
admin.site.register(Servicio)
admin.site.register(AutoServicio)
admin.site.register(Seguro)
admin.site.register(AutoSeguro)
admin.site.register(Garantia)
admin.site.register(AutoGarantia)
admin.site.register(RegistroMantenimiento)
admin.site.register(Reparacion)
admin.site.register(AutoReparacion)
