from configuredb import my_table, db

conn = db.connect()
select_statement = my_table.select()
result_set = conn.execute(select_statement)
print("-----------------")
for record in result_set:
    fecha_con_formato = record[3].strftime("%d-%m-%Y")
    print(f"Nombre:{record[0]}\nEdad:{record[1]}\n\
Activo:{record[2]}\nFecha de Nacimiento:{fecha_con_formato}")
    print("-----------------")
