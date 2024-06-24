#!/usr/bin/python3

import marshal
import dis


def load_module(file_path):
    with open(file_path, 'rb') as file:
        file.seek(16)  # Skip the header
        code = marshal.load(file)
    return code


def get_names_from_code(code):
    names = set()
    for instr in dis.get_instructions(code):
        if instr.opname == 'LOAD_GLOBAL' and not instr.argval.startswith('__'):
            names.add(instr.argval)
    return names


def main():
    code = load_module('hidden_4.pyc')
    names = get_names_from_code(code)
    sorted_names = sorted(names)
    for name in sorted_names:
        print(name)


if __name__ == "__main__":
    main()
