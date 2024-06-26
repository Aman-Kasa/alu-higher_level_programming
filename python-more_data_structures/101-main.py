#!/usr/bin/python3
square_matrix_map = __import__('101-square_matrix_map').square_matrix_map

matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2], [4, 5]],
    [[1, 2], [4, 5], [7, 8]],
    [[1]],
    [[1], [2], [3], [4]],
    [[]]
]

for matrix in matrices:
    new_matrix = square_matrix_map(matrix)
    print(new_matrix)
    print(matrix)
    print()
