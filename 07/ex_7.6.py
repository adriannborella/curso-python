from configuredb import my_table, db

conn = db.connect()
delete_statement = my_table.delete().where(my_table.c.nombre == 'pedro')
conn.execute(delete_statement)
