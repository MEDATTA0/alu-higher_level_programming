#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    for integer in reversed(my_list):
        print(str.format("{:d}".format(integer)))
