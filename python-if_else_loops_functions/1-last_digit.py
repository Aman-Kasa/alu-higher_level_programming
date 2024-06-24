#!/usr/bin/python3
import random

# Assign a random signed number to the variable `number`
number = random.randint(-10000, 10000)

# Determine the last digit of the number
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

# Print the appropriate message based on the value of the last digit
print(f"Last digit of {number} is {last_digit} and is ", end="")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
