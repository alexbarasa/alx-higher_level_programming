#!/usr/bin/python3
"""
Module: matrix_multiplication
This module provides a function to multiply two matrices using NumPy.

Functions:
    multiply_matrices(matrix1, matrix2):
        Multiply two matrices using NumPy.

"""

import numpy as np


def multiply_matrices(matrix1, matrix2):

    """
    Multiply two matrices using NumPy.

    Parameters:
    matrix1 : numpy.ndarray
        The first matrix to be multiplied.
    matrix2 : numpy.ndarray
        The second matrix to be multiplied.

    Returns:
    numpy.ndarray
        The result of multiplying the two matrices.
    """
    result = np.dot(matrix1, matrix2)
    return (result)
