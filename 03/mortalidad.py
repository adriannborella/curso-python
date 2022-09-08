datos = open("Z:\\03\\datos.csv", encoding='UTF-8')

# Forma utilizando FOR
for linea in datos.readlines():
    print(linea)

# Forma utilizando while
line = datos.readline()
while line != '':
    print(line)
    line = datos.readline()

datos.close()
