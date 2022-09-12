from django.contrib import admin
from apps.personas.models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento', 'activo']
