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
        self.size = size

    @property
    def size(self):
        """size

        initialize size

        """

        return self.__size

    @size.setter
    def size(self, value):
        """size

        set size

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area

        calculate area by finding the power of size

        """

        return self.__size ** 2
