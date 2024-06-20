#!/usr/bin/python3
import sys

number = "Holberton"

try:
    print(f"{int(number)} Battery street")
except ValueError as e:
    print(f"{number} Battery street")
    print(f"ValueError: {e}", file=sys.stderr)
