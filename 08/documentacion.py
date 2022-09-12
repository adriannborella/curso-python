# Comentario de una sola línea
'''
Al utilizar triple comillas dobles podremos
añadir saltos de línea a nuestro comentario.

Al utilizar comillas simples podemos utilizar comillas "dobles".
'''
"""
Al utilizar triple comillas dobles podremos
añadir saltos de línea a nuestro comentario.

Al utilizar comillas dobles podemos utilizar comillas 'simples'.
"""


def palindromo(sentencia):
    """Permite conocer si un str es, o no, un palíndromo."""

    sentencia = sentencia.lower().replace(' ', '')
    return sentencia == sentencia[::-1]


import ipdb

ipdb.set_trace()

print(palindromo.__doc__)
help(palindromo)