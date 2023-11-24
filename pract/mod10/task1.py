import re
import doctest


def is_correct_password(password):
    """
    Функция, проверяющая корректность введенного пароля
    Args:
        password (str): пароль

    Returns:
        bool: корректность данных

    >>> is_correct_password('rtG&3FG#Tr^e')
    True
    >>> is_correct_password('a^A1@*@1Aa')
    True
    >>> is_correct_password('oF^a1D@y5%e6')
    True
    >>> is_correct_password('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True

    >>> is_correct_password('пароль')
    False
    >>> is_correct_password('password')
    False
    >>> is_correct_password('qwerty')
    False
    >>> is_correct_password('lOngPa$$W0Rd')
    False
    """
    pattern = re.compile(r'^(?=.*[a-z].*[a-z])(?=.*\d)(?=.*[$^%@#&*])(?=(.*[$^%@#&*]){3,})(?!.*[,.!?]).{8,}$')
    return bool(re.match(pattern, password))


doctest.testmod(verbose=True)