#!/usr/bin/python3


def search_replace(my_list: list, search: int, replace: int):
    return [replace if x == search else x for x in my_list]
