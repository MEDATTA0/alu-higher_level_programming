#!/usr/bin/python3


def delete_at(my_list: list, idx=0):
    if 0 <= idx < len(my_list):
        return my_list[:idx] + my_list[idx:]
    else:
        return my_list
