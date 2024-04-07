#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.

Functions:
    matrix_divided(matrix, div): Divides all elements of a matrix by a number
                                and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int, float): The number to divide all elements by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                    if each row of the matrix does not have the same size,
                    or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        new matrix with all numbers divided by div.
    """

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(matrix_error)

    if not matrix or all(not row for row in matrix):
        raise TypeError(matrix_error)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(matrix_error)

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(matrix_error)

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
