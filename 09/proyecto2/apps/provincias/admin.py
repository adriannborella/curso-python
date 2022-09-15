from django.contrib import admin
from apps.provincias.models import Provincia, Municipio
# Register your models here.


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ["id", 'name', 'id_sincronizacion', 'pais']
    list_filter = ['pais']


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'id_sincronizacion']
