#!/usr/bin/python3
"""
Module my_list
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        return str(self)
