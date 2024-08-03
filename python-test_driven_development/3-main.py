#!/usr/bin/python3
import importlib.util
import sys

module_name = "3-say_my_name"
file_path = "./3-say_my_name.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
say_my_name = module.say_my_name

# Test cases
say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
try:
    say_my_name("John", 12)
except Exception as e:
    print(e)
try:
    say_my_name()
except Exception as e:
    print(e)
