#!/usr/bin/python3
"""
This module contains a function to print text with 2 new lines
after each of '.', '?', and ':' characters.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of '.', '?', and ':' characters.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""

    for letter in text:
        current_line += letter

        if letter not in [".", "?", ":"]:
            continue
        else:
            print(current_line.lstrip(" "), end="\n\n")
            current_line = ""

    if current_line:
        print(current_line.strip(" "), end="")
