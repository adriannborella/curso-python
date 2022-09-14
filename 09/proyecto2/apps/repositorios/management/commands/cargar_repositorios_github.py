from django.core.management.base import BaseCommand
from apps.repositorios.models import RepositorioGithub
import requests
import json
from tqdm import tqdm


class Command(BaseCommand):
    help = "Comando que importa repositorios desde una API"

    def get_repositorios(self):
        url = f"http://testjava.equality.coop:8601/repositories/"

        response = requests.get(url)
        result = json.loads(response.text)
        return result

    def handle(self, *args, **options):
        RepositorioGithub.objects.all().delete()
        resporitorios = self.get_repositorios()
        for record in tqdm(resporitorios):
            RepositorioGithub.objects.\
                create(**record)
