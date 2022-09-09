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
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)
except psycopg2.DatabaseError as e:
    print(f'Error {e}')
finally:
    if con:
        con.close()
