#!/usr/bin/python3
"""
A module for JSON deserialization.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Parameters:
        my_str : The JSON string to be deserialized into a Python object.

    Returns:
        object: A Python object represented by the JSON string.
    """

    return json.loads(my_str)
