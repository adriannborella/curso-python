import requests

url = 'https://www.ine.es/jaxi/files/tpx/es/csv_bdsc/50155.csv'
response = requests.get(url)

# with open("data.csv", "w") as f:
#     f.write(response.text)
#     f.close()

file = open("data.csv", "w")
file.write(response.text)
file.close()
