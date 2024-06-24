#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        # Check if it's the last pair to decide whether to print ", " or "\n"
        end = ", " if i < 8 and j < 9 else "\n"
        print("{:d}{:d}{}".format(i, j, end), end="")
