#!/usr/bin/python3
"""
Module base_geometry
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
