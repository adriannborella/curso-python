from clases import Encuesta, clase1, clase3, \
    clase2, clase4, clase5

datos = open("datos.csv", encoding='UTF-8')
datos.readline()
lista = [Encuesta(linea.split(';')) for linea in datos.readlines()]
lista[0].__str__()
datos.close()

print(lista)
