#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

def main():
    try:
        # Test case: Creating a square with size 5
        my_square = Rectangle.square(5)
        print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
        print(my_square)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

if __name__ == "__main__":
    main()
