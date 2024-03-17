#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves the element at the specified index in a list.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index in the list.
        Returns None if the index is out of range or negative.
    """

    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return my_list[idx]
