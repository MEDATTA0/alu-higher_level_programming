#!/usr/bin/python3


def no_c(my_string: str):
    if my_string is None:
        return ""
    splitted_my_string = my_string.split("c")
    splitted_my_string = "".join(splitted_my_string).split("C")
    return "".join(splitted_my_string)
