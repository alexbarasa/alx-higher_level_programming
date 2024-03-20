#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix:
        return

    def square(x):

        return lambda x: x**2
    new_matrix = matrix[:]
    # square = lambda x: x**2
    S = list(map(lambda lst: list(map(square(lst), lst)), new_matrix))
    return S
