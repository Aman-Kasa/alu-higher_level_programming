#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    # Create instances of Rectangle and print their areas
    r1 = Rectangle(3, 2)
    print(r1.area())  # Expected output: 6

    r2 = Rectangle(2, 10)
    print(r2.area())  # Expected output: 20

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())  # Expected output: 56
