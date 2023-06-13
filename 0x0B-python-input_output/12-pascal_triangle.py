#!/usr/bin/python3
"""
Contains the pascal_triangle function
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(i):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)

    return triangle
