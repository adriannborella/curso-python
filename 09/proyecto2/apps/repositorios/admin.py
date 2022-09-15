from django.contrib import admin
from apps.repositorios.models import RepositorioGithub, RepositorioPython


@admin.register(RepositorioGithub)
class RepositorioGithubAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'repo_name', 'created', 'language', 'days_alive']
    list_filter = ["stars", "forks", "days_alive"]


@admin.register(RepositorioPython)
class RepositorioPythonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'version']
