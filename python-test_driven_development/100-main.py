#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))  # Should print: [[7, 10], [15, 22]]
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))         # Should print: [[13, 16]]
