#!/usr/bin/python3

"""
2-matrix_divided module
=======================

Provides a function to divide all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists representing a matrix.
        div (int or float): The divisor to divide the elements by.

    Returns:
        list: A new matrix with elements divided by the divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
            or if each row of the matrix does not have the same size,
            or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
