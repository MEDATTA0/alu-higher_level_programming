#!/usr/bin/python3


def replace_in_list(my_list: list, idx: int, new_element: int):
    if 0 <= idx < len(my_list):
        my_new_list = my_list.copy()
        my_new_list[idx] = new_element
        return my_new_list
    else:
        return my_list
