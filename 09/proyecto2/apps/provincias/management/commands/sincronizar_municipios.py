from django.core.management.base import BaseCommand
from apps.provincias.models import Provincia, Municipio
import requests
import json


class Command(BaseCommand):
    help = "Comando que saluda"

    def get_municipios(self, id_provincia):
        url = f"https://apis.datos.gob.ar/georef/api/municipios?\
provincia={id_provincia}&campos=id,nombre&max=1000"

        response = requests.get(url)
        result = json.loads(response.text)
        # return result['municipios']
        return result.get('municipios', [])

    def handle(self, *args, **options):
        total = Provincia.objects.all().count()
        actual = 0
        Municipio.objects.all().delete()
        for provincia in Provincia.objects.all():
            actual += 1
            self.stdout.write(f"Sincronizanco {actual} de {total}")
            municipios = self.get_municipios(provincia.id_sincronizacion)

            for record in municipios:
                Municipio.objects.create(name=record.get("nombre"),
                                         id_sincronizacion=record.get("id"),
                                         provincia=provincia)
