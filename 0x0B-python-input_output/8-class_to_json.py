#!/usr/bin/python3
"""
A module contains a function that Returns a dictionary description suitable
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns a dictionary description suitable for JSON serialization
    of an object.

    Parameters:
        obj: An instance of a Class with serializable attributes.

    Returns:
        A dictionary containing serializable attributes of the object.
    """
    return obj.__dict__
