#!/usr/bin/python3

import sys


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Incorrect number of arguments. Usage: <num1> <operator> <num2>")
        sys.exit(1)

    # Extract arguments
    num1_str, operator, num2_str = sys.argv[1], sys.argv[2], sys.argv[3]

    # Validate and convert num1
    try:
        num1 = float(num1_str)
    except ValueError:
        print(f"Invalid number: {num1_str}")
        sys.exit(1)

    # Validate and convert num2
    try:
        num2 = float(num2_str)
    except ValueError:
        print(f"Invalid number: {num2_str}")
        sys.exit(1)

    # Perform the calculation based on the operator
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
    else:
        print(f"Invalid operator: {operator}")
        sys.exit(1)

    # Print the result
    print(f"The result of {num1} {operator} {num2} is: {result}")


if __name__ == "__main__":
    main()
