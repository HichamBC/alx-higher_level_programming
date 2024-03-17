#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific position
    without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index of the element to replace.
        element: The new element to insert at the specified index.

    Returns:
        list: A new list with the element replaced at the specified index,
              or the original list if the index is out of range.
    """

    # create a copy of the original list (my_list).
    n_list = my_list[:]

    if idx < 0:
        return n_list
    elif idx >= len(n_list):
        return n_list
    else:
        n_list[idx] = element
        return n_list
