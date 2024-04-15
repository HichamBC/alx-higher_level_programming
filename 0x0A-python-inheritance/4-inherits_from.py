#!/usr/bin/python3
"""
Provides a function to check if an object is an instance of a class
that inherited (directly or indirectly)  the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is a subclass of a class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare against.

    Returns:
        True if the object is a subclass of a class, False otherwise.
    """
    obj_class = obj.__class__
    mro = obj_class.mro()

    if obj_class != a_class:
        return any(cls is a_class for cls in mro)

    return False
