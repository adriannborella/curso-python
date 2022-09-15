# Generated by Django 4.1.1 on 2022-09-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repositorio_python',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('version', models.CharField(max_length=8, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Repositorio_python',
                'verbose_name_plural': 'Repositorio_pythons',
            },
        ),
    ]