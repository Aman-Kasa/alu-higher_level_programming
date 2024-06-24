#!/usr/bin/python3

# Import specific functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define variables a and b
a = 10
b = 5

# Define a function to print in the required format
def print_operation(op_name, result):
    print(f"{op_name}({a}, {b}) -> {result}")

# Perform arithmetic operations and print results
add_result = add(a, b)
print_operation("add", add_result)

sub_result = sub(add_result, b)
print_operation("sub", sub_result)

mul_result = mul(sub_result, b)
print_operation("mul", mul_result)

div_result = div(mul_result, b)
print_operation("div", div_result)
