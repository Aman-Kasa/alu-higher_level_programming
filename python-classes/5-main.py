#!/usr/bin/python3
"""
5-main module

This module tests the Square class defined in 5-square.py.

"""

if __name__ == "__main__":
    Square = __import__('5-square').Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
