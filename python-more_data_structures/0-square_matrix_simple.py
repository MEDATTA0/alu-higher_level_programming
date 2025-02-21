#!/usr/bin/python3

if __name__ == "__main__":

    def square_matrix_simple(matrix: list):
        return [[x**2 for x in row] for row in matrix]
