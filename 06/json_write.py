import json

# Diccionario Python
cliente = {
    "nombre": "Nora",
    "edad": 56,
    "id": "45355",
    "color_ojos": "verdes",
    "usa_lentes": False
}

# Abir (o crear) un archivo cliente.json
# y guardar la nueva versión de la información
with open("z:\\06\\cliente.json", 'w') as archivo_nuevo:
    json.dump(cliente, archivo_nuevo, indent=4)
