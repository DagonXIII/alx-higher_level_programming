#!/usr/bin/python3

class Square:
    """This class represents a square.

    The Square class accepts a size parameter and sets
    it to the private instance attribute __size.

    The __init__ method assigns the instance attribute size to the
    private instance attribute __size using the self keyword.

    Args:
        size (int): defines the size of the square.

    Attributes:
        __size (int): defines the size of the square as private.
    """

    def __init__(self, size):
        self.__size = size
