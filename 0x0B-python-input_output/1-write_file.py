#!/usr/bin/python3
"""
A module for file writing (UTF-8 encoded) operation.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoded) and returns
    the number of characters written.

    Parameters:
        filename (str, optional): file to which the string will be written.
                                  Default is an empty string.
        text (str, optional): The string to be written to the file.
                              Default is an empty string.

    Returns:
        The number of characters written to the file.

    """

    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
