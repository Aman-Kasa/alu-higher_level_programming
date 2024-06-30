#!/usr/bin/python3
"""
2-main module

This module tests the Square class defined in 2-square.py.

"""

if __name__ == "__main__":
    Square = __import__('2-square').Square

    # Test case 1: Create Square with size 3
    try:
        my_square_1 = Square(3)
        print(type(my_square_1))
        print(my_square_1.__dict__)
        print(my_square_1.size)  # Attempt to access size attribute
    except Exception as e:
        print(e)

    # Test case 2: Create Square with default size (0)
    try:
        my_square_2 = Square()
        print(type(my_square_2))
        print(my_square_2.__dict__)
        print(my_square_2.size)  # Attempt to access size attribute
    except Exception as e:
        print(e)

    # Test case 3: Create Square with non-integer size
    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
        print(my_square_3.size)  # Attempt to access size attribute
    except Exception as e:
        print(e)

    # Test case 4: Create Square with negative size
    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
        print(my_square_4.size)  # Attempt to access size attribute
    except Exception as e:
        print(e)
