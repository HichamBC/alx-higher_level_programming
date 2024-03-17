#!/usr/bin/python3
def no_c(my_string):
    """
    Remove all occurrences of characters 'c' and 'C' from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The modified string with 'c' and 'C' removed.
    """

    s = ""
    # Iterate through each character in the string
    for letter in my_string:
        # Check if the character is not 'c' or 'C'
        if letter != "c" and letter != "C":
            # Append the character to s
            s += letter

    # return the modified string s
    return s
