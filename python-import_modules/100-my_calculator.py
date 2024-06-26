#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    print("Script started")
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        # Extract and convert arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    print(f"Arguments received: a={a}, operator={operator}, b={b}")
    # Perform the operation
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    # Print the result
    print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    main()
