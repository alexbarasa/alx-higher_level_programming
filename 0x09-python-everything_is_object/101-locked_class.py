#!/usr/bin/python3
"""
The mudule ``01-locked_class`` consist of
A class that restricts the dynamic creation of instance attributes,
allowing only the attribute 'first_name' to be created.
"""


class LockedClass:
    """
    LockedClass

    A class that restricts the dynamic creation of instance attributes,
    allowing only the attribute 'first_name' to be created.

    Attributes:
        None

    Methods:
        __setattr__(self, name, value):
            Overrides the default behavior of setting instance attributes.
            Parameters:
                name (str): The name of the attribute being set.
                value (any): The value to be assigned to the attribute.
            Raises:
                AttributeError: If an attempt is made to create
                an instance attribute other than 'first_name'.

        """
    def __setattr__(self, name, value):
        """
        __setattr__(self, name, value):

        Overrides the default behavior of setting instance attributes.

        Parameters:
            name (str): The name of the attribute being set.
            value (any): The value to be assigned to the attribute.

        Raises:
            AttributeError: If an attempt is made to create
            an instance attribute other than 'first_name'.

        """
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has "
                                 "no attribute '{}'".format(name))
