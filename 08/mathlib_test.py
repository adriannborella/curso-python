import mathlib


def test_suma():
    """Verify the output of `suma` function"""
    esperado = 6
    obtenido = mathlib.suma(2, 4)
    assert esperado == obtenido


def test_resta():
    """Verify the output of `resta` function"""
    output = mathlib.resta(2, 4)
    assert output == -2


def test_multiplicacion():
    """Verify the output of `multiplicacion` function"""
    output = mathlib.multiplicacion(2, 4)
    assert output == 8
