#!/usr/bin/python3
"""

Rectangle module

"""


class Rectangle:
    """

    Rectangle

    """

    def __init__(self, width=0, height=0):
        """

        Initializes height and width

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """

        Returns the width of the rectangle

        """

        return self.__width

    @width.setter
    def width(self, value):
        """

        Set the width from value

        Args:
            value: The width of the rectangle

        Raises:
            TypeError: If `value` type not int.
            ValueError: If `value` is less than 0.

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """

        Returns height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """

        Sets height

        Args:
            value: height of the rectangle

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return f"{{'_Rectangle__height': {self._Rectangle__height}, '_Rectangle__width': {self._Rectangle__width}}}"
