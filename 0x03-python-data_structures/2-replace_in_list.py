#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
    Replace the element at the specified index in the given list.

    Args:
        my_list (list): The list in which to replace the element.
        idx (int): The index at which to replace the element.
        element: The new element to be placed at the specified index.

    Returns:
        list:modified list with the element replaced at the specified index.

    '''

    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
