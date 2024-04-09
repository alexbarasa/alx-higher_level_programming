#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer().  For example,

"""
def add_integer(a, b=98):

    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    return (a + b)
