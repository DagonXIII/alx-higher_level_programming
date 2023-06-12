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
        print(sorted(self))
