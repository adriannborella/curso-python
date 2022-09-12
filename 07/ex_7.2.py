from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData, Integer, Boolean, Date
import json

dbname = 'db_develop'
user = 'educando'
password = 'python2022'
host = '162.243.174.228'
port = 8610

db_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
print(db_string)
db = create_engine(db_string)
meta = MetaData(db)

my_table = Table('adrian-nicolas', meta, Column('nombre', String),
                 Column('edad', Integer), Column('activo', Boolean),
                 Column('fecha_naciento', Date))

my_table.create()
