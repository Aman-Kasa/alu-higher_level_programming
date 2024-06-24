#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))   # Output: "Bes School"
print(remove_char_at("Chicago", 2))       # Output: "Chcago"
print(remove_char_at("C is fun!", 0))     # Output: " is fun!"
print(remove_char_at("School", 10))       # Output: "School"
print(remove_char_at("Python", -2))       # Output: "Python"
