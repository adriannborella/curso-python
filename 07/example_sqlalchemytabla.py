from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData, Integer, Boolean, Date

dbname = 'db_develop'
user = 'educando'
password = 'python2022'
host = '162.243.174.228'
port = 8610

db_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
print(db_string)
db = create_engine(db_string)
meta = MetaData(db)

users_table = Table('adrian-nicolas', meta, Column('nombre', String),
                    Column('id', Integer), Column('username', String))

with db.connect() as conn:
    #Create Table
    # users_table.create()

    # Create
    insert_statement = users_table.insert().values(nombre="Doctor Strange",
                                                   username="Scott Derrickson")
    import ipdb; ipdb.set_trace()
    # result = cur.execute(
    #     "INSERT INTO usuarios (nombre, username) VALUES('Adrian2', 'adriannborella2');"
    # )
    conn.execute(insert_statement)
    # Read
    select_statement = users_table.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)

    # Update
    update_statement = users_table.update().where(
        users_table.c.nombre == "Doctor Strange").values(
            nombre="Doctor Strange - Modificado")
    conn.execute(update_statement)

    # Delete
    delete_statement = users_table.delete().where(users_table.c.id == 15)
    conn.execute(delete_statement)
