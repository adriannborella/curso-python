import json

with open("z:\\06\\conf_app.json") as file:
    datos = json.load(file)
    print(f"Nombre:{datos['nombre']}")
    print(f"Version:{datos['version']}")
    print(f"Nro max de Usuarios:{datos['cantidad_max_usuarios']}")
