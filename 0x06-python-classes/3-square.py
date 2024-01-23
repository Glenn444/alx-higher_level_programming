#!/usr/bin/python3
"""Class Square

Defines a square

"""


class Square:
    """Class Square

    Square class with private instance attribute

    """

    def __init__(self, size=0):
        """__init__ method initializes attributes of the object

        Args:
            size: private integer

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area

        calculates area by finding the power of size

        """

        return self.__size ** 2
