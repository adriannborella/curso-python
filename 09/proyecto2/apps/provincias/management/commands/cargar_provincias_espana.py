from django.core.management.base import BaseCommand
from apps.provincias.models import Provincia
import json


class Command(BaseCommand):
    help = "Comando que saluda"

    def handle(self, *args, **options):
        # self.stdout.write("Hola desde el comando")
        path = "provincias-espanolas.json"
        with open(path, encoding='UTF-8') as file:
            datos = json.load(file)
            for record in datos:
                fields = record.get('fields')
                nro_sincro = int(fields.get('codigo'))
                Provincia.objects.create(name=fields.get('provincia'),
                                         id_sincronizacion=nro_sincro,
                                         pais=2)
