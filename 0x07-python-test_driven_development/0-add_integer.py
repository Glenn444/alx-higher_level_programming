#!/usr/bin/python3
"""

Function to add integers

"""


def add_integer(a, b=98):
    """ Adds two integers

    Args:
        a (:obj:`int, float`): The first argument int
        b (:obj: `int, float`, optional): The second argument

    Returns:
        int: The result of the addition.

    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num):
    """ Converts float to int

    Cast a float to an integer number

    Args:
        num: argument

    """

    if type(num) is float:
        num = int(num)
    return num
