#!/usr/bin/python3

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
