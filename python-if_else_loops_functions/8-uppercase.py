#!/usr/bin/python3


def uppercase(string: str):
    upper_string = ""
    for char in string:
        if char.islower():
            upper_string += chr(ord(char) + 32)
        else:
            upper_string += char
    print(upper_string)
