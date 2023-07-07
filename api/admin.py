from django.contrib import admin

from api.models.usuario import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cedula_persona', 'nombres_persona', 'apellidos_persona', 'telefono_persona', 'email_usuario','texto','rol_usuario',)
    list_filter = ('rol_usuario',)
    search_fields = ('email_usuario',)