#!/usr/bin/python3


def delete_at(my_list: list, idx=0):
    if 0 <= idx < len(my_list):
        my_list = my_list[:idx].append(my_list[idx + 1 :])
        return my_list
    else:
        return my_list
