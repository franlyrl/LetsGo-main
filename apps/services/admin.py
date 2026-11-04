from django.contrib import admin
from .models import ServicioTuristico


@admin.register(ServicioTuristico)
class ServicioTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio_desde', 'ubicacion', 'destacado', 'activo')
    list_filter = ('categoria', 'destacado', 'activo')
    search_fields = ('nombre', 'descripcion', 'ubicacion')
