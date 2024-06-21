#!/usr/bin/python3

number = 25

try:
    result = number / 0  # Example of an operation that could raise an exception
    print(f"{result} Battery street")
except TypeError as e:
    print(
        f"[Got]\n{number} Battery street\n\n"
        f"[Expected]\nValueError: Unknown format code 'd' for object of type 'str'\n\n"
        f"[stderr]: {e}\n"
    )
except ValueError as e:
    print(
        f"[Got]\n{number} Battery street\n\n"
        f"[Expected]\n{result} Battery street\n\n"
        f"[stderr]: {e}\n"
    )
except ZeroDivisionError as e:
    print(
        f"[Got]\n{number} Battery street\n\n"
        f"[Expected]\n0 Battery street\n\n"
        f"[stderr]: {e}\n"
    )
except Exception as e:
    print(
        f"[Got]\n{number} Battery street\n\n"
        f"[Expected]\n-98 Battery street\n\n"
        f"[stderr]: {e}\n"
    )
