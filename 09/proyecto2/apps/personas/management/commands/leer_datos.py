from django.core.management.base import BaseCommand
from apps.personas.models import Persona
import json
from datetime import datetime


class Command(BaseCommand):
    help = "Comando que saluda"

    def handle(self, *args, **options):
        # self.stdout.write("Hola desde el comando")
        with open("datos.json", encoding='UTF-8') as file:
            datos = json.load(file)
            for record in datos:
                fecha_nacimiento = datetime.strptime(
                    record.get("fecha_nacimiento"), "%d/%m/%Y")
                Persona.objects.create(nombre=record.get("nombre"),
                                       apellido=record.get("apellido"),
                                       edad=record.get("edad"),
                                       direccion=record.get("nombre"),
                                       fecha_nacimiento=fecha_nacimiento,
                                       activo=record.get("activo"))
