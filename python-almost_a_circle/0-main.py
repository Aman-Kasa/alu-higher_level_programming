#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)  # Expected output: 1

    b2 = Base()
    print(b2.id)  # Expected output: 2

    b3 = Base()
    print(b3.id)  # Expected output: 3

    b4 = Base(12)
    print(b4.id)  # Expected output: 12

    b5 = Base()
    print(b5.id)  # Expected output: 4
