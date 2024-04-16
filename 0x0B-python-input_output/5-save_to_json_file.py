#!/usr/bin/python3
"""
A module for saving objects to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Parameters:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to which the JSON
                        representation will be saved.

    Returns:
        None
    """

    json_str = json.dumps(my_obj)

    with open(filename, "w", encoding="UTF8") as f:
        f.write(json_str)
