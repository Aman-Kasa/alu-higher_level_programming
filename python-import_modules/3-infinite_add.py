#!/usr/bin/python3

import sys


def main():
    # Get all arguments from sys.argv excluding the script name
    arguments = sys.argv[1:]
    
    # Initialize a variable to store the sum
    total_sum = 0
    
    # Iterate over each argument, convert it to int and add to total_sum
    for arg in arguments:
        total_sum += int(arg)
    
    # Print the result
    print(total_sum)


if __name__ == "__main__":
    main()
