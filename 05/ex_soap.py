from zeep import Client
import sys


def consultar_webservice(valor):
    client = Client(
        'https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')
    result = client.service.NumberToDollars(valor)
    return result


try:
    value = float(sys.argv[1])
    result = consultar_webservice(value)
    print(result)
except IndexError:
    print("No se envio el nro a consultar, por favor agreguelo como parametro\
al ejecutar el programa de la forma <nombre del programa>.py <Valor a buscar>")
except ValueError:
    print("Asegurese de enviar un parámetro numérico")
except Exception as ex:
    print(ex)
    print("Excepción no controlada, tipo de la excepción:")
    print(type(ex))
