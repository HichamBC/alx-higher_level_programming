#!/usr/bin/python3
def no_c(my_string):
    """
    Remove all occurrences of characters 'c' and 'C' from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The modified string with 'c' and 'C' removed.
    """

    # checks if my_string is empty
    if not my_string:
        # returns None of True
        return None

    # Initialize an empty string to store the result
    s = ""
    # checks if "c" or "C" exists in my_string.
    if "c" in my_string or "C" in my_string:
        # Iterate through each character in the string
        for letter in my_string:
            # Check if the character is not 'c' or 'C'
            if letter != "c" and letter != "C":
                # Append the character to s
                s += letter

        # return the modified string s
        return s

    # return the original string if any of "c" or "C" don't exist in it.
    return my_string
