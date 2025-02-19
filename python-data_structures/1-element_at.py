#!/usr/bin/python3


def element_at(my_list: list, idx: int):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None
