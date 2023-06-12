#!/usr/bin/python3
"""
Module 101-add_attribute
Defines a function add_attribute to add a new attribute to an object if possible
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible
    Args:
        obj (object): The object to add the attribute to
        attribute (str): The name of the attribute
        value (Any): The value of the attribute
    Raises:
        TypeError: If the object can't have new attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
