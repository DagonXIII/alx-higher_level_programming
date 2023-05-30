#!/usr/bin/python3
class Square:
    """This class represents a square.

    The Square class defines a square with a private instance attribute
    size. It allows for instantiation with an optional size parameter.

    Args:
        size (int, optional): The size of the square. Defaults to 0.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
