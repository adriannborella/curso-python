"""Módulo Main"""


class User(object):
    """Representa un usuario.

    Attributes:
        username (str): [Username]
        password (str): [Password]
    """

    def __init__(username: str, password: str) -> None:
        """Inicializa en objeto de tipo User.

        Args:
            username (str): [Username]
            password (str): [Password]
        """

        self.username = username
        self.password = password


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, un palindromo.

    Args:
        sentence (str)

    Returns:
        bool
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]