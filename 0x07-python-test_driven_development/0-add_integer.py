#!/usr/bin/python3
"""This module provides a function to add two numbers.

Functions:
    add_integer(a, b=98): Adds two numbers and returns the result as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result as an integer.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)
