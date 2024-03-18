#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence: The input string.

    Returns:
        tuple: A tuple containing the length of the string
                and its first character.
    """

    if not sentence:
        return 0, None

    return len(sentence), sentence[0]
