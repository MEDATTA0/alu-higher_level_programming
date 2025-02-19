#!/usr/bin/python3


def delete_at(my_list: list, idx):
    if 0 <= idx < len(my_list):
        my_list.pop(idx)
    else:
        return my_list
