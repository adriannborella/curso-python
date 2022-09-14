from configuredb import my_table, db

conn = db.connect()
delete_statement = my_table.delete().where(my_table.c.nombre == 'juan')
conn.execute(delete_statement)
