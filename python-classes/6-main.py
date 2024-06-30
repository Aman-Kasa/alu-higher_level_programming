#!/usr/bin/python3
"""
6-main module

This module tests the Square class defined in 6-square.py.

"""

if __name__ == "__main__":
    Square = __import__('6-square').Square

    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
