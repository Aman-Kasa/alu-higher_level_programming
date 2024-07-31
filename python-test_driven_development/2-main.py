#!/usr/bin/python3
"""
    Main script to test the matrix_divided function.
"""

from matrix_divided import matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Test cases
print(matrix_divided(matrix, 3))
print(matrix)

# Additional test cases
try:
    print(matrix_divided(matrix, 0))
except ZeroDivisionError as e:
    print(e)

try:
    print(matrix_divided(matrix, '2'))
except TypeError as e:
    print(e)

try:
    print(matrix_divided([[1, 2], [3]], 2))
except TypeError as e:
    print(e)

try:
    print(matrix_divided('not a matrix', 2))
except TypeError as e:
    print(e)
