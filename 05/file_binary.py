import requests

url = 'https://www.ine.es/jaxi/files/tpx/es/xlsx/50155.xlsx'
response = requests.get(url)

with open("data.xlsx", "wb") as f:
    f.write(response.content)
    f.close()
