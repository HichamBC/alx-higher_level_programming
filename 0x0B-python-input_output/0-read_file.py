#!/usr/bin/python3
"""
A module for reading text files (UTF8) and printing their content to stdout.
"""


def read_file(filename=""):
    """
    Reads the content of a text file (encoded in UTF-8) and prints it.

    Parameters:
        filename (str, optional): The name of the text file to be read.
                                  Default is an empty string.

    Returns:
        None
    """
    with open(filename, encoding="UTF8") as f:
        print(f.read())
