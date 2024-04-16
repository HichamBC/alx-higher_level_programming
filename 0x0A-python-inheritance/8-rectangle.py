#!/usr/bin/python3
"""
Defines a class representing a rectangle and the class BaseGeometry
it inherits from.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def area(self):
        """
        Raises:
            Exception: If the method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it is an integer and greater than 0.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are less than or equal to 0.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
