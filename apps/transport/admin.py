from django.contrib import admin
from .models import Transporte


@admin.register(Transporte)
class TransporteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'empresa', 'origen', 'destino', 'tarifa', 'activo')
    list_filter = ('tipo', 'activo', 'empresa')
    search_fields = ('nombre', 'descripcion', 'empresa', 'origen', 'destino')
