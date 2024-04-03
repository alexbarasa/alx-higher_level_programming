#!/usr/bin/python3
"""
This is the square class which will have different methods
Methods will be implemented later but this is just a prototype
of square
"""


class Square:
    """
    A class representing a square.

    This class allows the creation of square objects with specified
    side lengths.
    Squares are geometric shapes with four equal sides and four right angles.

    Attributes:
        size (int): The length of each side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with the specified side length.

        Args:
            size (int, optional): The length of each side of the square.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Example:
            >>> square = Square(5)
            >>> square.size
            5
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.

        Returns:
            int: The length of each side of the square.

        Example:
            >>> square = Square(5)
            >>> square.size
            5
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Args:
            value (int): The length of each side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Example:
            >>> square = Square(5)
            >>> square.size = 6
            >>> square.size
            6
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.

        Example:
            >>> square = Square(5)
            >>> square.area()
            25
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        Example:
            >>> square = Square(3)
            >>> square.my_print()
            ###
            ###
            ###
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
