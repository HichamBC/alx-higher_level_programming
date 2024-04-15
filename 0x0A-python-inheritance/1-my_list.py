#!/usr/bin/python3
"""
Defines a class that inherits from the built-in list class.
"""


class MyList(list):
    """
    class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list elements in sorted order (ascending).
        """
        sorted_list = sorted(self)
        print(sorted_list)
