from configuredb import my_table, db
import json

with open("z:\\07\\datos.json") as file:
    datos = json.load(file)
    conn = db.connect()
    for record in datos:
        insert_statement = my_table.insert().values(
            nombre=record.get("nombre"),
            edad=record.get("edad"),
            activo=record.get("activo"),
            fecha_naciento=record.get("fecha_naciento"))
        conn.execute(insert_statement)
