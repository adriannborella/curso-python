# Generated by Django 4.1.1 on 2022-09-15 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositorios', '0002_repositorio_python'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Repositorio_python',
            new_name='RepositorioPython',
        ),
        migrations.AlterModelOptions(
            name='repositoriopython',
            options={'verbose_name': 'Pypi', 'verbose_name_plural': 'Repositorio_pythons'},
        ),
    ]
