#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of list of int): The matrix to be printed.

    Returns:
        None

    Format:
        The function prints the matrix with each row on a separate line.
        Integers in each row are separated by a space.
    """
    for row in matrix:
        if len(row) == 0:
            print()
        for column in row:
            if row.index(column) != len(row) - 1:
                print("{:d}".format(column), end=" ")
            else:
                print("{:d}".format(column))
