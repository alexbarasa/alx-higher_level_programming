#!/usr/bin/python3

"""
Module: matrix_multiplication

This module provides a function to perform matrix multiplication.

Functions:
    matrix_mul(m_a, m_b): Multiplies two matrices.

    Args:
        m_a (list): Matrix A represented as a
        list of lists of integers or floats.
        m_b (list): Matrix B represented as a
        list of lists of integers or floats.

    Returns:
        list: Resultant matrix of the multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
        contains non-integer/float elements, or is not a rectangle.
        ValueError: If m_a or m_b is empty or cannot be multiplied.

"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): Matrix A represented as a list of
        lists of integers or floats.
        m_b (list): Matrix B represented as a list of
        lists of integers or floats.

    Returns:
        list: Resultant matrix of the multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
        contains non-integer/float elements, or is not a rectangle.
        ValueError: If m_a or m_b is empty or cannot be multiplied.

    """

    # Validate input matrices
    def validate_matrix(matrix):
        if not isinstance(matrix, list):
            raise TypeError("m_a must be a list or m_b must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("m_a must be a list of lists or m_b "
                            "must be a list of lists")
        if not matrix:
            raise ValueError("m_a can't be empty or m_b can't be empty")
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise TypeError("Each row of m_a must be of the same size or "
                                "each row of m_b must be of the same size")
            if not all(isinstance(elem, (int, float)) for elem in row):
                raise TypeError("m_a should contain only integers or floats or"
                                " m_b should contain only integers or floats")

    validate_matrix(m_a)
    validate_matrix(m_b)

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return (result)
