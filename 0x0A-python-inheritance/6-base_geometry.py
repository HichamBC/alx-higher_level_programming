#!/usr/bin/python3
"""
defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    A BaseGeometry class with public method area.
    """

    def area(self):
        """
        Raises:
            Exception: If the method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

