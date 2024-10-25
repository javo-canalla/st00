from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # Campos a mostrar en la lista de usuarios
    list_display = ('username', 'email', 'nombre', 'apellido', 'tipo_de_usuario', 'is_staff')
    # Campos por los que se puede filtrar
    list_filter = ('tipo_de_usuario', 'is_staff', 'is_superuser', 'is_active', 'groups')
    # Campos de búsqueda
    search_fields = ('username', 'email', 'nombre', 'apellido')
    # Campos para ordenar
    ordering = ('username',)

    # Configuración de los campos en la vista de detalle del usuario
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información Personal'), {'fields': ('nombre', 'apellido', 'email', 'direccion_email', 'numero_telefono_particular', 'numero_de_interno')}),
        (_('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Fechas Importantes'), {'fields': ('last_login', 'date_joined')}),
        (_('Información Adicional'), {'fields': ('tipo_de_usuario',)}),
    )

    # Configuración de los campos en la vista de creación de usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'nombre', 'apellido', 'email', 'direccion_email', 'numero_telefono_particular', 'numero_de_interno', 'tipo_de_usuario', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
