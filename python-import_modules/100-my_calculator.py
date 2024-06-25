#!/usr/bin/python3
import sys
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div


def calculator():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
    except ValueError:
        print("Error: Invalid input. <a> and <b> must be integers.")
        sys.exit(1)

    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            if b == 0:
                print("Error: division by zero")
                sys.exit(1)
            result = div(a, b)
        print(f"{a} {operator} {b} = {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculator()
