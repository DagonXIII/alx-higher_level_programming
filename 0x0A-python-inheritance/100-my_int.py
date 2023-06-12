#!/usr/bin/python3
"""
Module 100-my_int
Defines a class MyInt that inherits from int
"""


class MyInt(int):
    """
    A class that represents a rebel integer
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the == operator
        Args:
            other (Any): The object to compare with
        Returns:
            True if the objects are not equal, False otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator
        Args:
            other (Any): The object to compare with
        Returns:
            True if the objects are equal, False otherwise
        """
        return super().__eq__(other)
