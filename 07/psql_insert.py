import psycopg2

engine = psycopg2

dbname = 'db_develop'
user = 'educando'
password = 'python2022'
host = '162.243.174.228'
port = 8610

try:
    con = engine.connect(f"dbname='{dbname}' user='{user}' host='{host}' \
    password='{password}' port={port}")
    cur = con.cursor()
    result = cur.execute(
        "INSERT INTO usuarios (nombre, username) VALUES('Adrian2', 'adriannborella2');"
    )
    con.commit()  #Importante hacer un commit
    print(result)
except psycopg2.DatabaseError as e:
    print(f'Error {e}')
finally:
    if con:
        con.close()
