#!/usr/bin/env python3
magic_calculation = __import__('102-magic_calculation').magic_calculation

print(magic_calculation(1, 2, 3))   # Expected output: 5 (since 1 < 2, return 3)
print(magic_calculation(4, 3, 10))  # Expected output: 7 (since 10 > 3, return 4 + 3)
print(magic_calculation(4, 5, 10))  # Expected output: 10 (default case, return 4 * 5 - 10)
