def palindromo(sentencia):
    """Permite conocer si un str es, o no, un palíndromo.

    >>> palindromo('Anita lava la tina')
    True
    >>> palindromo('Se van sus naves')
    True
    >>> palindromo('PyWombat')
    False
    """

    sentencia = sentencia.lower().replace(' ', '')
    return sentencia == sentencia[::-1]


print(palindromo("hola"))
