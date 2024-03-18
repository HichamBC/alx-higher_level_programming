#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Remove the element at the specified index from the list.

    Args:
        my_list: The list from which to delete the element.
        idx: The index of the element to be removed.

    Returns:
        The modified list after removing the element at the specified index.
        If index is out of bounds or list is empty, original list is returned.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
