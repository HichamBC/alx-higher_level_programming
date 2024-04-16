#!/usr/bin/python3
"""
A module for generating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Retunrs a Pascal's triangle.

    Parameters:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)

    return triangle
