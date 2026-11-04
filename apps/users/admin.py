from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('telefono', 'direccion', 'biografia', 'foto_perfil')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'telefono', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'telefono')
