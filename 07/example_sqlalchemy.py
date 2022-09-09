from sqlalchemy import create_engine

dbname = 'db_develop'
user = 'educando'
password = 'python2022'
host = '162.243.174.228'
port = 8610

db_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
print(db_string)
db = create_engine(db_string)

result_set = db.execute("SELECT * FROM usuarios")
for r in result_set:
    print(r)
