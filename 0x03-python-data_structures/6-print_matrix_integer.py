#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if not matrix:
        return
    for row in matrix:
        for column in row:
            print(str.format("{:d}", column), end='')
            if column != row[-1]:
                print(" ", end='')
        print()
