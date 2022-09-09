import json

# Diccionario Python
cliente = {
    "nombre": "Nora",
    "edad": 56,
    "id": "45355",
    "color_ojos": "verdes",
    "usa_lentes": False
}
print(cliente)
# Obtener una cadena de caracteres JSON
cliente_JSON = json.dumps(cliente)
print(cliente_JSON)
