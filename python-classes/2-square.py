#!/usr/bin/python3
"""
Your module is documented
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initializes the square with a private instance attribute size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        pass
