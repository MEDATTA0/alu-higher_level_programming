#!/usr/bin/python3
"""
Your module is documented
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initializes the square with a private instance attribute size."""
        self.__size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size**2

    def my_print(self):
        """Prints "#" __size times"""
        print("\n".join("#" * self.__size for _ in range(self.__size)))


Square(3).my_print()
