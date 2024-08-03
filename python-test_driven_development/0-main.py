#!/usr/bin/python3
from 0-add_integer import add_integer

def main():
    print(add_integer(1, 2))        # Expected output: 3
    print(add_integer(100, -2))     # Expected output: 98
    print(add_integer(2))           # Expected output: 100
    print(add_integer(100.3, -2))   # Expected output: 98

    try:
        print(add_integer("a", 1))  # Expected to raise TypeError
    except Exception as e:
        print(e)

    try:
        print(add_integer(None))    # Expected to raise TypeError
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
