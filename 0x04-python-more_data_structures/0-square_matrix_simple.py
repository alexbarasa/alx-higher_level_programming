#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix:
        return
    new_matrix = matrix[:]
    square = lambda x: x**2
    S = list(map(lambda sublist: list(map(square, sublist)), new_matrix))
    return S
