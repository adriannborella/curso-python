from django.db import models


class RepositorioGithub(models.Model):
    repo_name = models.fields.CharField("Nombre", max_length=100)
    full_name = models.fields.CharField("Nombre Completo", max_length=150)
    created = models.fields.DateTimeField()
    language = models.fields.CharField("Lenguaje", max_length=10, null=True)
    username = models.fields.CharField("Usuario", max_length=100)
    stars = models.fields.IntegerField()
    forks = models.fields.IntegerField()
    subscribers = models.fields.IntegerField(null=True)
    open_issues = models.fields.IntegerField(null=True)
    days_alive = models.fields.IntegerField()

    class Meta:
        verbose_name = 'RepositorioGithub'
        verbose_name_plural = 'RepositorioGithubs'

    def __str__(self) -> str:
        return self.full_name