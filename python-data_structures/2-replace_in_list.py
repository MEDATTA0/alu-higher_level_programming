#!/usr/bin/python3


def element_at(my_list: list, idx: int, new_element: int):
    if 0 <= idx < len(my_list):
        my_list[idx] = new_element
        return my_list
    else:
        return None
