import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
import ipdb

ipdb.set_trace()
print(response.json())
