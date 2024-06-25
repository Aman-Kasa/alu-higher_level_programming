#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:  # Check if the row is not empty
            for i in range(len(row)):
                if i < len(row) - 1:
                    print("{:d}".format(row[i]), end=" ")
                else:
                    print("{:d}".format(row[i]))
        else:
            print()  # Print an empty line for empty rows

    if matrix and matrix[-1]:
        print("--")


if __name__ == "__main__":
    matrix_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2], [4, 5]],
        [[1, 2], [4, 5], [7, 8]],
        [[1]],
        [[1], [2], [3], [4]],
        [[]]
    ]

    for matrix in matrix_cases:
        print_matrix_integer(matrix)
