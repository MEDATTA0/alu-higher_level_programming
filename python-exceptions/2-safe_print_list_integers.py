#!/usr/bin/python3


def safe_print_list_integers(my_list: list, x: int):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                pass
    except IndexError as index_err:
        return index_err
    print()
    return count
