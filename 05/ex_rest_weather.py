import requests

url = "https://bestweather.p.rapidapi.com/weather/Madrid,%20Espa%C3%B1a/today"

querystring = {"unitGroup": "metric"}

headers = {
    "X-RapidAPI-Key": "fbaec21470mshbba54ac796bee11p19d802jsn4953d53ae394",
    "X-RapidAPI-Host": "bestweather.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

aux= response.json()
aux['days'][0]['temp']
import ipdb; ipdb.set_trace()