#!/usr/bin/python3
"""
Your module is documented
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initializes the square with a private instance attribute size."""

        try:
            if not isinstance(size, int):
                raise TypeError()
            elif size < 0:
                raise ValueError()
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        pass
