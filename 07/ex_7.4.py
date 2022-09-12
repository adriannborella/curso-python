from configuredb import my_table, db

conn = db.connect()
select_statement = my_table.select()
result_set = conn.execute(select_statement)
for r in result_set:
    print(r)
