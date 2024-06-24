#!/usr/bin/python3

import sys


def main():
    # Get the arguments passed to the script
    argv = sys.argv

    # Calculate the number of arguments (excluding the script name itself)
    num_args = len(argv) - 1

    # Print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    else:
        if num_args == 1:
            print(f"1 argument:")
        else:
            print(f"{num_args} arguments:")

        # Print each argument with its position
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")


if __name__ == "__main__":
    main()
