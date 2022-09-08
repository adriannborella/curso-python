import ipdb
import requests

api_url = "http://testjava.equality.coop:8601/repositories/"
response = requests.get(api_url)
ipdb.set_trace()
aux = response.json()

old_repository = aux[0]

for record in aux:
    if record['days_alive'] > old_repository['days_alive']:
        old_repository = record

print(old_repository)
