from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Comando que saluda"

    def handle(self, *args, **options):
        self.stdout.write("Hola")