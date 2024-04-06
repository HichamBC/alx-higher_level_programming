#!/usr/bin/python3
"""
This module defines a class named Square.
"""


class Square:
    """
    A class to define a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square object with the given size.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.size = size

    def area(self):
        """
        Calculate the area of a square.

        Returns:
            The area of the square.
    """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square of '#' characters based on the size attribute.

        If the size attribute is 0, prints an empty line. Otherwise,
        prints a square of '#' characters with dimensions equal to
        the value of the size attribute.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                for _ in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            The size of the object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
        value (int): The new size to set.

        Raises:
            TypeError: If the value provided is not an integer.
            ValueError: If the value provided is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
