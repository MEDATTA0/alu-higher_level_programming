#!/usr/bin/python3


def square_matrix_simple(my_list: list, search, replace):
    return [replace if x == search else x for x in my_list]
