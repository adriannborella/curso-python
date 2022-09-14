from configuredb import my_table, db
import json

with open("z:\\07\\datos.json", encoding='UTF-8') as file:
    datos = json.load(file)
    conn = db.connect()
    for record in datos:
        insert_statement = my_table.insert().values(
            nombre=record.get("nombre"),
            edad=record.get("edad"),
            activo=record.get("activo"),
            fecha_nacimiento=record.get("fecha_nacimiento"))
        conn.execute(insert_statement)

