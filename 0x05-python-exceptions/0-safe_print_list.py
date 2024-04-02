#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints the elements of a list up to a specified index.

    Args:
        my_list : The list to print elements from. Defaults to an empty list.
        x : The number of elements to print from the list. Defaults to 0.

    Returns:
        The number of elements printed.
    """
    num = 0

    try:
        for _ in range(x):
            print(my_list[num], end="")
            num += 1
    except exception:
        pass
    finally:
        print()

    return num
