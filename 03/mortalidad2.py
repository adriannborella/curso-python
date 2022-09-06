

datos = open("datos.csv", encoding='UTF-8')
lista = [linea for linea in datos.readlines()]

datos = open("datos.csv", encoding='UTF-8')
diccionario = {c: len(c) for c in datos.readlines()}

datos.close()

print(lista)
print(diccionario)
