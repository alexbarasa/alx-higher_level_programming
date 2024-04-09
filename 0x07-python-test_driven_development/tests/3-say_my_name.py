#!/usr/bin/python3

"""
This module has a function that prints your name
on standard output.
"""


def say_my_name(first_name, last_name=""):
    """
    Print your name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name is a string, otherwise raise a TypeError
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string, otherwise raise a TypeError
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    print("My name is {:s} {:s}".format(first_name, last_name))
