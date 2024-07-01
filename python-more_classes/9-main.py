#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

def main():
    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)

if __name__ == "__main__":
    main()
