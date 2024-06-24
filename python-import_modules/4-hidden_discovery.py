#!/usr/bin/python3

import dis
import marshal


def main():
    with open("hidden_4.pyc", "rb") as f:
        f.seek(16)  # skip the header of the .pyc file
        code = marshal.load(f)

    for name in sorted(code.co_names):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
