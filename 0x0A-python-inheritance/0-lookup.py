#!/usr/bin/python3
"""
Provides a function for inspecting the attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj (object): The object to inspect.

    Returns:
    A list containing the names of attributes and methods of the object.
    """
    return dir(obj)
