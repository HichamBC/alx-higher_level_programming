#!/usr/bin/python3
"""
Provides a function to perform type checking on objects.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare against.

    Returns:
        True if the object is an instance of the class, False otherwise.
    """
    return type(obj) is a_class
