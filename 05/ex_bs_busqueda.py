from bs4 import BeautifulSoup
import requests

payload = {'q': "astro"}
response = requests.get("https://pypi.org/search", params=payload)

soup = BeautifulSoup(response.text, features="html.parser")
result = []

records = soup.find_all('h3', class_='package-snippet__title')
import ipdb; ipdb.set_trace()
for record in records:
    name = record.find(class_='package-snippet__name')
    version = record.find(class_='package-snippet__version')
    result.append(f"{name.getText()} {version.getText()}")

for record in result:
    print(record)
