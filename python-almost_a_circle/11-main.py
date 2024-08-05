#!/usr/bin/python3
""" 11-main """
from models.square import Square


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)  # Output: [Square] (1) 0/0 - 5

    s1.update(10)
    print(s1)  # Output: [Square] (10) 0/0 - 5

    s1.update(1, 2)
    print(s1)  # Output: [Square] (1) 0/0 - 2

    s1.update(1, 2, 3)
    print(s1)  # Output: [Square] (1) 3/0 - 2

    s1.update(1, 2, 3, 4)
    print(s1)  # Output: [Square] (1) 3/4 - 2

    s1.update(x=12)
    print(s1)  # Output: [Square] (1) 12/4 - 2

    s1.update(size=7, y=1)
    print(s1)  # Output: [Square] (1) 12/1 - 7

    s1.update(size=7, id=89, y=1)
    print(s1)  # Output: [Square] (89) 12/1 - 7
