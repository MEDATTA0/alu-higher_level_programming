#!/usr/bin/python3


def multiply_by_2(a_dictionary: dict):
    new_a_dictionary = {}
    for key in a_dictionary.keys():
        new_a_dictionary[key] = a_dictionary[key] * 2
    return new_a_dictionary
