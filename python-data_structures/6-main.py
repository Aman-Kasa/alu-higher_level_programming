#!/usr/bin/python3

# Function to print a matrix of integers
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        first = True
        for num in row:
            if not first:
                print(" ", end="")
            else:
                first = False
            print("{:d}".format(num), end="")
        print()

# Test cases
if __name__ == "__main__":
    # Example matrices
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2], [4, 5]]
    matrix3 = [[1, 2], [4, 5], [7, 8]]
    matrix4 = [[1]]
    matrix5 = [[1], [2], [3], [4]]
    matrix6 = [[]]

    # Print each matrix using print_matrix_integer function
    print_matrix_integer(matrix1)
    print("--")
    print_matrix_integer(matrix2)
    print("--")
    print_matrix_integer(matrix3)
    print("--")
    print_matrix_integer(matrix4)
    print("--")
    print_matrix_integer(matrix5)
    print("--")
    print_matrix_integer(matrix6)
