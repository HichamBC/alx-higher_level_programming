#!/usr/bin/python3
"""
Provides a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
