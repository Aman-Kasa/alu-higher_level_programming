#!/usr/bin/python3

import dis
import sys
import types

# Load the bytecode from the downloaded file
with open('hidden_4.pyc', 'rb') as file:
    bytecode = file.read()

# Define a function to collect names from bytecode
def collect_names(code):
    names = set()
    instructions = dis.get_instructions(code)
    for instr in instructions:
        if instr.starts_line and instr.opname == 'LOAD_NAME' and not instr.argval.startswith('__'):
            names.add(instr.argval)
    return names

# Create a dummy module to execute the bytecode
module = types.ModuleType('hidden_module')
code = module.__loader__.code_from_bytes(bytecode)
exec(code, module.__dict__)

# Get names from the module's namespace
module_names = [name for name in module.__dict__ if not name.startswith('__')]

# Get names from bytecode
bytecode_names = collect_names(code)

# Combine and sort names
all_names = sorted(module_names + list(bytecode_names))

# Print each name on a new line
for name in all_names:
    print(name)
