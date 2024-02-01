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

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    x = int(a)
    y = int(b)
    return x + y
