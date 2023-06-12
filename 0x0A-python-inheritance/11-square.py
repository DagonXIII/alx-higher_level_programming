#!/usr/bin/python3
"""
Module 11-square
Defines a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square
    """

    def __init__(self, size):
        """
        Initializes a Square instance
        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
