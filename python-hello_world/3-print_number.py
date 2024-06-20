#!/usr/bin/python3
number = "Holberton"

try:
    print(f"{int(number)} Battery street")
except ValueError:
    print(f"{number} Battery street")
