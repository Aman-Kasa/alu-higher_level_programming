#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)        # Output: [Square] 13/13
print(s.area()) # Output: 169 (since area of square with side length 13 is 13 * 13)
