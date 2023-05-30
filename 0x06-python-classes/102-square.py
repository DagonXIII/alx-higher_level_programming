#!/usr/bin/python3
"""
Module - Square
Class definition for a Square
"""


class Square:
    """
    Class - Square
    Represents a square
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size
        Args:
            size (int or float): The size of the square (default: 0)
        Raises:
            TypeError: If size is not a number
            ValueError: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        Args:
            value (int or float): The size of the square
        Raises:
            TypeError: If value is not a number
            ValueError: If value is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the area of the current square is equal to the area of another square
        Args:
            other (Square): Another square object
        Returns:
            True if areas are equal, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if the area of the current square is not equal to the area of another square
        Args:
            other (Square): Another square object
        Returns:
            True if areas are not equal, False otherwise
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than the area of another square
        Args:
            other (Square): Another square object
        Returns:
            True if current square's area is greater, False otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than or equal to the area of another square
        Args:
            other (Square): Another square object
        Returns:
            True if current square's area is greater than or equal, False otherwise
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the area of the current square is less than the area of another square
        Args:
            other (Square): Another square object
        Returns:
            True if current square's area is less, False otherwise
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the current square is less than or equal to the area of another square
        Args:
            other (Square): Another square object
        Returns:
            True if current square's area is less than or equal, False otherwise
        """
        return self.area() <= other.area()
