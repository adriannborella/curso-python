# Generated by Django 4.1.1 on 2022-09-14 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provincias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('id_sincronizacion', models.IntegerField()),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provincias.provincia')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
    ]
