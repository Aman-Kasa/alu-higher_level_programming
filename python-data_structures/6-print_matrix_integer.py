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
    if matrix:
        print("--")


if __name__ == "__main__":
    matrix0 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix1 = [[1, 2], [4, 5]]
    matrix2 = [[1, 2], [4, 5], [7, 8]]
    matrix3 = [[1]]
    matrix4 = [[1], [2], [3], [4]]
    matrix5 = [[]]

    print_matrix_integer(matrix0)
    print_matrix_integer(matrix1)
    print_matrix_integer(matrix2)
    print_matrix_integer(matrix3)
    print_matrix_integer(matrix4)
    print_matrix_integer(matrix5)
