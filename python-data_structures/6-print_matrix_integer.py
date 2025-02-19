#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for element in line:
            print(str.format("{}".format(element)), end=" ")
        print("")


print(print_matrix_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
