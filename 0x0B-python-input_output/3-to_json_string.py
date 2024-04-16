#!/usr/bin/python3
"""
A module for JSON serialization.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Parameters:
        my_obj: The object to be serialized to a JSON string.

    Returns:
        A JSON string representing the serialized object.
    """
    return json.dumps(my_obj)
