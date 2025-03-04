#!/usr/bin/python3
"""
Your module is documented
"""


class Square:
    def __init__(self, size=0):
        try:
            if isinstance(size) != int:
                raise TypeError()
            elif size < 0:
                raise ValueError()
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        pass
