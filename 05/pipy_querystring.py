import requests

payload = {'q': "astro"}
response = requests.get("https://pypi.org/search", params=payload)
# https://pypi.org/search/?q=astro
# https://pypi.org/search/?q=astro

import ipdb; ipdb.set_trace()

print(response.text)
print(response.url)
