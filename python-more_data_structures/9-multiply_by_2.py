#!/usr/bin/python3


def multiply_by_2(a_dictionary: dict):
    for key in a_dictionary.keys():
        a_dictionary[key] *= 2
    return a_dictionary
