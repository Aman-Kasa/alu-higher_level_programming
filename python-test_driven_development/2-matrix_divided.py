#!/usr/bin/python3
'''A function that divides a matrix by a number'''


def matrix_divided(matrix, div):
    """A function that divides a matrix by a number"""
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Check if matrix is empty or contains empty rows
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        if len(matrix) == 1 and len(matrix[0]) == 0:
            return [[]]
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Check if all elements in the matrix are integers or floats
    if not all(isinstance(item, (int, float)) for row in matrix
               for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Check if all rows are of the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]

    return new_matrix
