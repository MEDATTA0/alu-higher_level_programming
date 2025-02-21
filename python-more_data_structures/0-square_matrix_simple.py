#!/usr/bin/python3

if __name__ == "__main__":

    def square_matrix_simple(matrix: list):
        new_matrix = []
        for i in matrix:
            if isinstance(i, list):
                temporary_matrix = []
                for j in i:
                    temporary_matrix.append(j**2)
                new_matrix.append(temporary_matrix)
            else:
                new_matrix.append(i**2)

        return new_matrix
