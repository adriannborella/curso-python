import requests


response = requests.get("https://pypi.org")
import ipdb; ipdb.set_trace()
type(response)
print(response.text)
print(response.status_code)

print(requests.codes.ok)
