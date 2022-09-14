from django.contrib import admin
from apps.personas.models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'fecha_nacimiento', 'activo']
    search_fields = ['nombre', 'apellido']
    list_filter = ['fecha_nacimiento', 'activo']
    fields = (('nombre', 'apellido'), ('fecha_nacimiento', 'edad'), 'activo',
              'direccion')
