#!/usr/bin/python3


def divisible_by_2(my_list: list):
    if len(my_list) == 0:
        return None
    bool_list = []
    for number in my_list:
        if number % 2 == 1:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
