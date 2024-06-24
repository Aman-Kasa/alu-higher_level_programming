#!/usr/bin/python3

# Import specific functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define variables a and b
a = 10
b = 5

# Perform arithmetic operations
add_result = add(a, b)
sub_result = sub(add_result, b)
mul_result = mul(sub_result, b)
div_result = div(mul_result, b)

# Print the results in the specified format
print("{a} + {b} = {add_result}".format(a=a, b=b, add_result=add_result))
print("{a} - {b} = {sub_result}".format(a=add_result, b=b, sub_result=sub_result))
print("{a} * {b} = {mul_result}".format(a=sub_result, b=b, mul_result=mul_result))
print("{a} / {b} = {div_result}".format(a=mul_result, b=b, div_result=div_result))
