#!/usr/bin/python3


def best_score(a_dictionary: dict):
    if a_dictionary is None:
        return None
    the_best = 0
    the_name = ""
    for key in a_dictionary.keys():
        if the_best < a_dictionary[key]:
            the_name = key
            the_best = a_dictionary[key]
    return the_name
