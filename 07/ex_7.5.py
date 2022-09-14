from configuredb import my_table, db, ejecutar_sentencia

# conn = db.connect()
# conn.execute(update_statement)
import ipdb; ipdb.set_trace()
update_statement = my_table.update().where(
    my_table.c.nombre == "pedro").values(activo=False)
ejecutar_sentencia(update_statement)
