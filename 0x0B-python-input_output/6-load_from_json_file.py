#!/usr/bin/python3
"""
A module for loading objects from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
        filename (str): the JSON file from which the object will be created.

    Returns:
        The Python object created from the JSON data in the file.
    """

    with open(filename, encoding="UTF8") as f:
        return json.load(f)
