#!/usr/bin/python3

import sys


def main():
    if len(sys.argv) != 4:
        print("Incorrect number of arguments. Usage: <num1> <operator> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
    except ValueError:
        print(f"Invalid number: {sys.argv[1]}")
        sys.exit(1)

    operator = sys.argv[2]
    valid_operators = ['+', '-', '*', '/']

    if operator not in valid_operators:
        print(f"Invalid operator: {operator}")
        sys.exit(1)

    try:
        num2 = float(sys.argv[3])
    except ValueError:
        print(f"Invalid number: {sys.argv[3]}")
        sys.exit(1)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Division by zero is not allowed")
            sys.exit(1)
        result = num1 / num2

    print(f"The result of {num1} {operator} {num2} is: {result}")


if __name__ == "__main__":
    main()
