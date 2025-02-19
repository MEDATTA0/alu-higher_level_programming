#!/usr/bin/python3


def max_integer(my_list: list):
    if my_list is None:
        return None
    else:
        max = 0
        for number in my_list:
            if number > max:
                max = number
        return max
