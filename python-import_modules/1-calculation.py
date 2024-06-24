#!/usr/bin/python3

# Import specific functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define variables a and b
a = 10
b = 5

# Perform arithmetic operations and store results
add_result = add(a, b)
sub_result = sub(add_result, b)
mul_result = mul(sub_result, b)
div_result = div(mul_result, b)

# Format the output according to the specified format
output = (
    f"{a} + {b} = {add_result}",
    f"{add_result} - {b} = {sub_result}",
    f"{sub_result} * {b} = {mul_result}",
    f"{mul_result} / {b} = {div_result}"
)

# Print each line of the formatted output
for line in output:
    print(line)
