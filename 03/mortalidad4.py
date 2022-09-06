from clases import Encuesta
import ipdb

datos = open("datos.csv", encoding='UTF-8')
datos.readline()
lista = [Encuesta(linea.split(';')) for linea in datos.readlines()]
lista[0].__str__()
datos.close()

ipdb.set_trace()

print(lista)
