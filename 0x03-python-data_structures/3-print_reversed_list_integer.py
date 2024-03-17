#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    Print the elements of a list in reverse order.

    Args:
        my_list (list): The list to be printed in reverse order.

    Returns:
        None

    '''

    if not my_list:
        return None

    for num in reversed(my_list):
        print("{:d}".format(num))
