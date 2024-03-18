#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list.

    Args:
        my_list: The input list of integers.

    Returns:
        The biggest integer in the list, or None if the list is empty.
    """

    if not my_list:
        return None

    biggest = 0
    for num in my_list:
        if num > biggest:
            biggest = num

    return biggest
