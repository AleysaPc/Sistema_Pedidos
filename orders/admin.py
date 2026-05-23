from django.contrib import admin
from .models import Orden, DetalleOrden, HistorialOrden

admin.site.register(Orden)
admin.site.register(DetalleOrden)   
admin.site.register(HistorialOrden)
