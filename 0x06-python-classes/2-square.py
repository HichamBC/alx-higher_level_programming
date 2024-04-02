#!/usr/bin/python3
"""
This module defines a class named Square.
"""


class Square:
    """
    A class to define a square.

    Attributes:
        __size: The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square object with the given size.

        Args:
            size: The size of the square.

        Returns:
            None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
