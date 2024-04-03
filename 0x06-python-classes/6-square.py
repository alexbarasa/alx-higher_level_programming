#!/usr/bin/python3
"""
This is the square class which will have different methods
Methods will be implemented later but this is just a prototype
of square
"""


class Square:
    """
    A class representing a square.

    This class allows the creation of square objects with
    specified side lengths
    and positions.

    Attributes:
        size (int): The length of each side of the square.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with the specified side length
        and position.

        Args:
            size (int, optional): The length of each side of the square.
            Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position
            is not a tuple of 2
            positive integers.
            ValueError: If size is less than 0 or position contains
            negative values.

        Example:
            >>> square = Square(5, (2, 3))
            >>> square.size
            5
            >>> square.position
            (2, 3)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for retrieving the position attribute.

        Returns:
            tuple: The position of the square.

        Example:
            >>> square = Square(5, (2, 3))
            >>> square.position
            (2, 3)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position attribute.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains negative values.

        Example:
            >>> square = Square(5)
            >>> square.position = (2, 3)
            >>> square.position
            (2, 3)
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            >>> square = Square(3, (1, 2))
            >>> square.my_print()
              ###
              ###
              ###
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
