#!/usr/bin/python3
"""
This module provides a function to perform type checking on objects
based on class hierarchy.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class or superclass to compare against.

    Returns:
        True if obj is an instance of a class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
