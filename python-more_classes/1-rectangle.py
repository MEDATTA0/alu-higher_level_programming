#!/usr/bin/python3

"""
Your module is documented
"""


class Rectangle:
    """{}"""

    def __init__(self, height, width):
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        """Setter for width with validation."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def width(self, value):
        """Setter for height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    pass
