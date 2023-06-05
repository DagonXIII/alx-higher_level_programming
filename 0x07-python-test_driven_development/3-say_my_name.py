#!/usr/bin/python3

"""
3-say_my_name module
=====================

Provides a function to print a name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to an empty string.

    Raises:
        TypeError: If the first name or last name is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob")
        My name is Bob
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = first_name
    if last_name:
        name += " " + last_name

    print("My name is", name)
