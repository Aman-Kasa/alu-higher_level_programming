#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    operations = [
        {"op": "add()", "result": add(a, b)},
        {"op": "sub()", "result": sub(a, b)},
        {"op": "mul()", "result": mul(a, b)},
        {"op": "div()", "result": div(a, b)}
    ]

    for op in operations:
        next_op_index = (operations.index(op) + 1) % len(operations)
        next_next_op_index = (operations.index(op) + 2) % len(operations)

        print(f"a = {a} and b = {b} FAKE : "
              f"- {op['op']} -> {operations[next_op_index]['op']} "
              f"- {operations[next_op_index]['op']} -> {op['op']} "
              f"- {op['op']} -> {operations[next_next_op_index]['op']} "
              f"- {operations[next_next_op_index]['op']} -> {op['op']}")
