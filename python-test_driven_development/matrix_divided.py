#!/usr/bin/python3
"""
    This module contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and round to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with divided values rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix is not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all elements of the matrix are integers or floats
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix is the same size
    row_lengths = {len(row) for row in matrix}
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element by div and round to 2 decimal places
    return [[round(item / div, 2) for item in row] for row in matrix]
