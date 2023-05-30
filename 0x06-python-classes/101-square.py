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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position
        Args:
            size (int): The size of the square (default: 0)
            position (tuple): The position of the square (default: (0, 0))
        Raises:
            TypeError: If size is not an integer
                      If position is not a tuple of 2 positive integers
            ValueError: If size is less than 0
        """
        self.size = size
        self.position = position

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
            value (int): The size of the square
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square
        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square
        Args:
            value (tuple): The position of the square
        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'
        If size is equal to 0, prints an empty line
        Uses position to adjust the position of the square
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return self.my_print()
