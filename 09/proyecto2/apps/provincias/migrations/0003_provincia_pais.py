# Generated by Django 4.1.1 on 2022-09-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provincias', '0002_municipio'),
    ]

    operations = [
        migrations.AddField(
            model_name='provincia',
            name='pais',
            field=models.IntegerField(choices=[(1, 'Argentina'), (2, 'España'), (3, 'Otro')], default=1),
        ),
    ]
