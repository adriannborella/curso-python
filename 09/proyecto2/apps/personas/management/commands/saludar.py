from django.core.management.base import BaseCommand
from apps.personas.models import Persona


class Command(BaseCommand):
    help = "Comando que saluda"

    def handle(self, *args, **options):
        # self.stdout.write("Hola desde el comando")
        for record in Persona.objects.all():
            self.stdout.write(str(record))
