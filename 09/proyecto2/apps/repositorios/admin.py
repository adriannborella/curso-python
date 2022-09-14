from django.contrib import admin
from apps.repositorios.models import RepositorioGithub


@admin.register(RepositorioGithub)
class RepositorioGithubAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'repo_name', 'created', 'language', 'days_alive']
