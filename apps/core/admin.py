from django.contrib import admin
from .models import Sugerencia


@admin.register(Sugerencia)
class SugerenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'creada_en', 'leida')
    list_filter = ('leida', 'creada_en')
    search_fields = ('nombre', 'email', 'mensaje')
