#!/usr/bin/python3
"""
A module for file writing (UTF-8 encoded) operation.
"""


def append_write(filename="", text=""):
    """
    appends a string to a the end of a text file (UTF-8 encoded)
    and returns the number of characters written.

    Parameters:
        filename (str, optional): file to which the string will be appended to.
                                  Default is an empty string.
        text (str, optional): The string to be appended to the file.
                              Default is an empty string.

    Returns:
        The number of characters appended to the file.

    """

    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
