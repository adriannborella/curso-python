from django.core.management.base import BaseCommand
from apps.provincias.models import Provincia


class Command(BaseCommand):
    help = "Comando que saluda"

    def handle(self, *args, **options):
        with open("provincias.csv", encoding='UTF-8') as file:
            file.readline()
            lines = file.readlines()
            for record in lines:
                fields = record.split(",")
                nro_sincro = int(fields[4].replace('"', ''))
                Provincia.objects.create(name=fields[7].replace('"', ''),
                                         id_sincronizacion=nro_sincro)
            file.close()
