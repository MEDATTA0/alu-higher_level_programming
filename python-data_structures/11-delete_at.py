#!/usr/bin/python3


def delete_at(my_list: list, idx):
    if 0 <= idx < len(my_list):
        del my_list[idx]
        return my_list
    else:
        return my_list
