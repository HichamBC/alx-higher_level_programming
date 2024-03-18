#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Check if each element in the given list is divisible by 2.

    Args:
        my_list: The list of integers to check.

    Returns:
        A list of boolean values indicating whether each element
        in my_list is divisible by 2.
    """
    return [True if num % 2 == 0 else False for num in my_list]
