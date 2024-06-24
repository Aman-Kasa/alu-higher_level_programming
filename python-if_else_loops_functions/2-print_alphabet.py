#!/usr/bin/python3
# Print the ASCII alphabet in lowercase without a newline at the end
print("{}".format(
    "".join(chr(c) for c in range(97, 123))  # Generate and join lowercase letters
), end="")  # Ensure no newline at the end
