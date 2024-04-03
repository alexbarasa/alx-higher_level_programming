#!/usr/bin/python3
"""
This is the square class which will have different methods
Methods will be implemented later but this is just a prototype
of square
"""


class Square:

    """
    A class representing a square.

    This class can be used to create square objects with specified properties.

    Attributes:
        No attributes are defined yet.
    """
    def __init__(self, size=0):

        """
        Initializes a Square object with the specified side length.

        Args:
            size (float or int): The length of each side of the square.

        Example:
            >>> square = Square(5)
            >>> square.size
            5
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
