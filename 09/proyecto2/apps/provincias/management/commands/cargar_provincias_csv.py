from django.core.management.base import BaseCommand
from apps.provincias.models import Provincia
import csv


class Command(BaseCommand):
    help = "Comando que lee archivo y carga los nuevos registros en la db"

    def handle(self, *args, **options):
        with open('provincias.csv', 'r', encoding='utf8') as csvfile:
            # creating dictreader object
            file = csv.DictReader(csvfile)
            for row in file:
                Provincia.objects.create(nombre=row['nombre'],
                                         id_sincronizacion=row['id'])
