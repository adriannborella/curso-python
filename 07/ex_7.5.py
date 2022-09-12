from configuredb import my_table, db

conn = db.connect()
update_statement = my_table.update().where(my_table.c.nombre == "juan").values(
    activo=False)
conn.execute(update_statement)
