#!/usr/bin/python3
"""Class Square

Defines a square

"""


class Square:
    """Class Square

    Square class with private instance attribute

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method initializes attributes of the object

        Args:
            size: private integer
            position: tuple of two positive int

        """
        self.size = size
        self.position = position

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

        Args:
            value: int to be set

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position

        returns position

        """
        return self.__position

    @position.setter
    def position(self, value):
        """position

        sets position

        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area

        calculate area by finding the power of size

        """

        return self.__size ** 2

    def my_print(self):
        """my_print

        method to print a square

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
