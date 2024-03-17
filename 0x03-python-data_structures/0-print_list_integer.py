#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints each integer in the input list on a separate line.

    Args:
        my_list (list): The list of integers to be printed.

    Returns:
        None
    """

    for i in my_list:
        print("{:d}".format(i))
