#!/usr/bin/python3
"""
Contains the to_json_string function
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj (object): The object to be serialized.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
