from django.core.management.base import BaseCommand
from apps.repositorios.models import RepositorioPython
import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm


class Command(BaseCommand):
    help = "Comando que importa repositorios desde una API"

    def extraer_pagina(self, pagina):
        url = f"https://pypi.org/search/?c=Framework+%3A%3A+Scrapy&o=&q=&page={pagina}"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")
        result = []
        records = soup.find_all('h3', class_='package-snippet__title')
        for record in records:
            name = record.find(class_='package-snippet__name')
            version = record.find(class_='package-snippet__version')
            result.append({'name': name.text, 'version': version.text})
        return result

    def get_repositorios(self):
        url = f"https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Scrapy"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")
        result = []

        btns_pages = soup.find_all('a', class_='button-group__button')
        nro_pages = int(btns_pages[-2].text)

        for cnt in tqdm(range(nro_pages)):
            repos = self.extraer_pagina(cnt + 1)
            result += repos

        return result

    def handle(self, *args, **options):
        RepositorioPython.objects.all().delete()
        repositorios = self.get_repositorios()
        for record in repositorios:
            RepositorioPython.objects.create(**record)
