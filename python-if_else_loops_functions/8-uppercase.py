#!/usr/bin/python3


def uppercase(string: str):
    upper_string = ""
    for char in string:
        if "a" <= char <= "z":
            upper_string += chr(ord(char) - 32)
        else:
            upper_string += char
    print("{}".format(upper_string))
