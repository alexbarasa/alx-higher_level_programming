#!/usr/bin/python3

"""
This script contains unit tests for the max_integer function.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
    Test cases for the max_integer function.
    """

    def test_upper(self):
        """
        Test case to check if max_integer returns the
        maximum value from a list of positive integers.
        """
        self.assertEqual(max_integer([6, 7, 8, 9]), 9)

    def test_none(self):
        """
        Test case to check if max_integer returns None
        when an empty list is passed.
        """
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """
        Test case to check if max_integer returns the
        only element in a list containing a single element.
        """
        self.assertEqual(max_integer([2]), 2)

    def test_one_neg(self):
        """
        Test case to check if max_integer returns the only
        element in a list containing a single negative element.
        """
        self.assertEqual(max_integer([-10]), -10)

    def test_neg(self):
        """
        Test case to check if max_integer returns the maximum
        positive value when negative values are present.
        """
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)

    def test_middle(self):
        """
        Test case to check if max_integer returns the maximum
        value from a list with the maximum value not at the beginning or end.
        """
        self.assertEqual(max_integer([1, 3, 8, 2, 6]), 8)


if __name__ == '__main__':
    unittest.main()
