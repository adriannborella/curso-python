from django.core.management.base import BaseCommand
from apps.repositorios.models import RepositorioGithub
import requests
import json
from tqdm import tqdm
import csv


class Command(BaseCommand):
    help = "Comando que importa repositorios desde una API"

    def clear_dict(self, obj):
        result = obj.__dict__
        del result['_state']
        return result

    def handle(self, *args, **options):
        registros = RepositorioGithub.objects.all()

        with open('example.csv', 'w', newline='') as csvfile:
            my_writer = csv.writer(csvfile, delimiter=';')

            primero = self.clear_dict(registros.first())
            cabecera = primero.keys()
            my_writer.writerow(cabecera)

            for record in tqdm(registros):
                a_escribir = self.clear_dict(record)
                my_writer.writerow(a_escribir.values())
